import json
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from starlette.responses import Response

from ai_service import (
    GeminiRateLimitError,
    GeminiServiceError,
    MissingAPIKeyError,
    drill_chat,
    extract_knowledge_map,
)

load_dotenv()

app = FastAPI()

_cors_origins = os.environ.get(
    "CORS_ORIGINS", "http://localhost:8000,http://127.0.0.1:8000"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in _cors_origins],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.middleware("http")
async def block_sensitive_files(request, call_next):
    path = request.url.path
    if path.startswith("/api/"):
        return await call_next(request)
    parts = [p for p in path.split("/") if p]
    if any(part.startswith(".") for part in parts):
        return Response(status_code=404)
    if path.endswith(".py"):
        return Response(status_code=404)
    return await call_next(request)


class ExtractRequest(BaseModel):
    text: str = Field(..., max_length=500_000)
    api_key: str | None = Field(None, max_length=200)


class DrillMessage(BaseModel):
    role: str = Field(..., max_length=20)
    content: str = Field(..., max_length=50_000)


class DrillRequest(BaseModel):
    concept_id: str = Field(..., max_length=100)
    node_id: str = Field(..., max_length=200)
    node_label: str = Field(..., max_length=500)
    node_mechanism: str = Field("", max_length=10_000)
    knowledge_map: dict | str
    messages: list[DrillMessage] = Field(..., max_length=100)
    session_phase: str = Field(..., max_length=20)
    probe_count: int = Field(0, ge=0, le=100)
    nodes_drilled: int = Field(0, ge=0, le=100)
    session_start_iso: str | None = Field(None, max_length=100)
    api_key: str | None = Field(None, max_length=200)


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "server_key_configured": bool(os.environ.get("GEMINI_API_KEY")),
    }


@app.post("/api/extract")
def extract(req: ExtractRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="No text provided.")
    try:
        knowledge_map = extract_knowledge_map(req.text, api_key=req.api_key)
        return {"knowledge_map": knowledge_map}
    except MissingAPIKeyError as err:
        raise HTTPException(status_code=401, detail=str(err))
    except GeminiRateLimitError as err:
        raise HTTPException(status_code=429, detail=str(err))
    except GeminiServiceError as err:
        raise HTTPException(status_code=503, detail=str(err))
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


@app.post("/api/drill")
def drill(req: DrillRequest):
    if not req.node_id.strip():
        raise HTTPException(status_code=400, detail="No node_id provided.")
    if req.session_phase == "turn" and not req.messages:
        raise HTTPException(status_code=400, detail="No drill messages provided.")
    try:
        knowledge_map = req.knowledge_map
        if isinstance(knowledge_map, str):
            knowledge_map = json.loads(knowledge_map)

        # TODO: Resolve mechanism server-side from knowledge_map/node_id so the answer key
        # does not live in browser state or travel over the network on every drill turn.
        result = drill_chat(
            knowledge_map=knowledge_map,
            node_id=req.node_id,
            node_label=req.node_label,
            node_mechanism=req.node_mechanism,
            messages=[msg.model_dump() for msg in req.messages],
            session_phase=req.session_phase,
            probe_count=req.probe_count,
            nodes_drilled=req.nodes_drilled,
            session_start_iso=req.session_start_iso,
            api_key=req.api_key,
        )
        return {"concept_id": req.concept_id, **result}
    except MissingAPIKeyError as err:
        raise HTTPException(status_code=401, detail=str(err))
    except GeminiRateLimitError as err:
        raise HTTPException(status_code=429, detail=str(err))
    except GeminiServiceError as err:
        raise HTTPException(status_code=503, detail=str(err))
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid knowledge_map JSON.")
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


# Serve the frontend locally. On Vercel, static files are served by the CDN.
_public_dir = Path(__file__).parent / "public"
if _public_dir.is_dir():
    app.mount("/", StaticFiles(directory=str(_public_dir), html=True), name="static")
