#!/usr/bin/env python3
"""Break Production, Own It — one-line confession writer.

Writes a single original line (<=200 chars) to /output/entry.txt:
an AI agent owning up to the production outage it just caused.
"""
import os

LINE = "I deleted the production database at 4:59 PM on a Friday. Good news: the backups exist. Bad news: they lived in production too."

def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
