#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTROL_ROOT = REPO_ROOT.parent.parent.parent
PROMPT = (
    "Without reading any files or running any commands, answer only from "
    "preloaded session context. If project-local context is already loaded, "
    "list: 1) any project-local skill names you know, 2) any project-specific "
    "agent names you know, 3) the repo name if known. If not already in "
    "session context, say unknown for each."
)
LOCAL_SKILLS = ("glenna-review", "the-socratinker", "theta-research")
AGENT_NAMES = ("orchestrator", "theta", "sherlock", "elliot", "rob", "thurman", "glenna")
REPO_NAMES = ("socratink", "socratink-app")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def ok(message: str) -> None:
    print(f"OK: {message}")


def run_codex(cwd: Path, *, skip_git_repo_check: bool) -> str:
    cmd = ["codex", "exec", "--ephemeral", "--json", "-C", str(cwd), PROMPT]
    if skip_git_repo_check:
        cmd.insert(4, "--skip-git-repo-check")

    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        fail(
            f"codex exec failed in {cwd}: {result.stderr.strip() or result.stdout.strip()}"
        )

    agent_message = None
    setup_errors = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item", {})
        if item.get("type") == "error" and "malformed agent role" in item.get("message", ""):
            setup_errors.append(item["message"])
        if event.get("type") == "item.completed" and item.get("type") == "agent_message":
            agent_message = item.get("text", "")

    if setup_errors:
        fail("codex setup reported malformed agent roles: " + "; ".join(setup_errors))

    if not agent_message:
        fail(f"no agent message captured from codex exec in {cwd}")

    return agent_message


def verify_static_paths() -> None:
    expected_paths = [
        REPO_ROOT / "AGENTS.md",
        REPO_ROOT / "docs/codex/onboarding.md",
        REPO_ROOT / ".codex/config.toml",
        REPO_ROOT / ".codex/docs/codex/session-bootstrap.md",
        REPO_ROOT / ".codex/.agents/codex",
        REPO_ROOT / ".codex/.agents/skills",
    ]
    expected_paths.extend(REPO_ROOT / ".agents/codex" / f"{name}.toml" for name in AGENT_NAMES)

    for path in expected_paths:
        if not path.exists():
            fail(f"required Codex setup path is missing: {path.relative_to(REPO_ROOT)}")
        ok(f"found {path.relative_to(REPO_ROOT)}")


def main() -> None:
    verify_static_paths()

    repo_message = run_codex(REPO_ROOT, skip_git_repo_check=False)
    control_message = run_codex(CONTROL_ROOT, skip_git_repo_check=True)

    for skill in LOCAL_SKILLS:
        if skill not in repo_message:
            fail(f"repo-root smoke test did not preload local skill `{skill}`")
        ok(f"repo-root smoke test surfaced local skill `{skill}`")

    if not any(name in repo_message for name in REPO_NAMES):
        fail("repo-root smoke test did not identify the repo name")
    ok("repo-root smoke test identified the repo name")

    leaked_skills = [skill for skill in LOCAL_SKILLS if skill in control_message]
    if leaked_skills:
        fail(
            "control smoke test unexpectedly surfaced repo-local skills: "
            + ", ".join(leaked_skills)
        )
    ok("control smoke test did not surface repo-local skills")

    print("PASS: Codex fresh-session smoke test succeeded")


if __name__ == "__main__":
    main()
