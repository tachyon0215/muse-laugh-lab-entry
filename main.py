#!/usr/bin/env python3
"""Write the One-Liner Laugh Lab entry line to entry.txt.

Deterministic, standard library only, no network.
The prompt answered: the excuse a robot vacuum gives after eating
a sock. The vacuum pleads jurisdiction - the sock was on the floor
plan, the floor is its jurisdiction, and everything there gets
filed internally. Deadpan bureaucracy, in the machine's own voice.
"""
import os
from pathlib import Path

LINE = "In my defence, the sock was on the floor plan, the floor is my jurisdiction, and everything in my jurisdiction eventually gets filed internally."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
