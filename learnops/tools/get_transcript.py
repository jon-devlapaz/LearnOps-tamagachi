#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pyperclip
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from youtube_transcript_api import YouTubeTranscriptApi

console = Console()

DEFAULT_OUTPUT_DIR = Path(
    os.environ.get(
        "GET_TRANSCRIPT_OUTPUT_DIR",
        "~/Desktop/Obsidian Vault/transcripts",
    )
).expanduser()


def sanitize_filename(title: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*]', "", title).strip()
    return (safe or "transcript")[:100]


def extract_video_id(url: str) -> str | None:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path_parts = [part for part in parsed.path.split("/") if part]

    if "youtu.be" in host:
        return path_parts[0] if path_parts else None

    if "youtube.com" in host or "youtube-nocookie.com" in host:
        query = parse_qs(parsed.query)
        if "v" in query and query["v"]:
            return query["v"][0]

        if len(path_parts) >= 2 and path_parts[0] in {"live", "shorts", "embed", "v"}:
            return path_parts[1]

        if len(path_parts) >= 2 and path_parts[0] == "watch":
            return path_parts[1]

    return None


def get_metadata(video_id: str) -> dict[str, str]:
    try:
        url = f"https://youtube.com/watch?v={video_id}"
        cmd = [
            "yt-dlp",
            "--skip-download",
            "--print",
            "%(title)s|||%(uploader)s|||%(duration)s",
            url,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, check=False)

        if result.returncode == 0:
            parts = result.stdout.strip().split("|||")
            duration = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0
            mins = duration // 60
            return {
                "title": parts[0] if len(parts) > 0 and parts[0] else "Unknown",
                "uploader": parts[1] if len(parts) > 1 and parts[1] else "Unknown",
                "duration": f"{mins} min" if duration else "Unknown",
            }
    except Exception:
        pass

    return {"title": "Unknown", "uploader": "Unknown", "duration": "Unknown"}


def fetch_transcript(video_id: str) -> str:
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.fetch(video_id)
    return " ".join(segment.text for segment in transcript_list)


def save_transcript(
    video_url: str,
    metadata: dict[str, str],
    full_text: str,
    output_dir: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = output_dir / f"{sanitize_filename(metadata['title'])}.txt"

    with filename.open("w", encoding="utf-8") as file_handle:
        file_handle.write(f"Title: {metadata['title']}\n")
        file_handle.write(f"Channel: {metadata['uploader']}\n")
        file_handle.write(f"Duration: {metadata['duration']}\n")
        file_handle.write(f"URL: {video_url}\n")
        file_handle.write(f"\n{'=' * 60}\n\n")
        file_handle.write(full_text)

    return filename


def maybe_copy_to_clipboard(full_text: str, enabled: bool) -> str:
    if not enabled:
        return "disabled"

    try:
        pyperclip.copy(full_text)
        return "transcript copied"
    except pyperclip.PyperclipException:
        return "unavailable"


def extract_transcript(video_url: str, output_dir: Path, copy_to_clipboard: bool = True) -> int:
    video_id = extract_video_id(video_url)
    if not video_id:
        console.print("[red]Invalid YouTube URL[/red]")
        return 1

    with console.status("[cyan]Fetching metadata...[/cyan]"):
        metadata = get_metadata(video_id)

    with console.status("[cyan]Fetching transcript...[/cyan]"):
        try:
            full_text = fetch_transcript(video_id)
        except Exception as exc:
            console.print(f"[red]Could not get transcript: {exc}[/red]")
            console.print("[dim](Video might not have captions enabled)[/dim]")
            return 1

    filename = save_transcript(video_url, metadata, full_text, output_dir)
    clipboard_status = maybe_copy_to_clipboard(full_text, copy_to_clipboard)

    table = Table.grid(padding=(0, 2))
    table.add_column(style="bold dim")
    table.add_column()
    table.add_row("Title", metadata["title"])
    table.add_row("Channel", metadata["uploader"])
    table.add_row("Duration", metadata["duration"])
    table.add_row("Length", f"{len(full_text):,} characters")
    table.add_row("Saved", str(filename))
    table.add_row("Clipboard", clipboard_status)

    console.print()
    console.print(Panel(table, title="[green]Done[/green]", border_style="green"))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Fetch a YouTube transcript and save it to a text file."
    )
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument(
        "-o",
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help=f"Directory where transcript files are written (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--no-clipboard",
        action="store_true",
        help="Do not copy the transcript text to the clipboard.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    url = args.url
    if not url:
        url = console.input("\n[bold]YouTube URL:[/bold] ").strip()

    if not url:
        console.print("[red]No URL provided[/red]")
        return 1

    return extract_transcript(
        video_url=url,
        output_dir=Path(args.output_dir).expanduser(),
        copy_to_clipboard=not args.no_clipboard,
    )


if __name__ == "__main__":
    raise SystemExit(main())
