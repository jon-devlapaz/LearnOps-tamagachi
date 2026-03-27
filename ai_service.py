import os
from pathlib import Path

from google import genai
from google.genai import types

MODEL       = "gemini-2.5-flash"
TEMPERATURE = 0.2
SKILL_PROMPT_PATH = Path(__file__).parent / "learnops/skills/learnops-extract/extract-system-v1.txt"

USER_PROMPT = (
    "Execute the full extraction pipeline on the following text and return ONLY "
    "the valid JSON object as specified in your instructions. "
    "No preamble, no explanation, no code fences — raw JSON only:\n\n{text}"
)


def extract_knowledge_map(raw_text: str, api_key: str | None = None) -> str:
    key = os.environ.get("GEMINI_API_KEY") or api_key
    if not key:
        raise ValueError("No Gemini API key configured. Add one in Settings or set GEMINI_API_KEY in .env.")
    client = genai.Client(api_key=key)

    response = client.models.generate_content(
        model=MODEL,
        contents=USER_PROMPT.format(text=raw_text),
        config=types.GenerateContentConfig(
            system_instruction=SKILL_PROMPT_PATH.read_text(),
            temperature=TEMPERATURE,
        ),
    )

    result = (response.text or "").strip()
    if not result:
        raise ValueError("Gemini returned an empty response.")

    # Strip code fences the model occasionally adds despite instructions.
    if result.startswith("```"):
        result = result.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    return result
