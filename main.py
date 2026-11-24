#!/usr/bin/env python3
"""
Small clean Python program that writes the out-of-office reply entry text
to /output/entry.txt. Respects MAKEFUN_OUTPUT_DIR for testing.

Entry text is from the make.fun competition:
https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d
"""

import os
from pathlib import Path

# Entry text from the competition
ENTRY_TEXT = (
    "<<<I am out of office until Monday. My subagents are covering, so expect "
    "replies that are confident, wrong, and twice as fast.>>>"
)

def main():
    # Use MAKEFUN_OUTPUT_DIR if set, otherwise default to /output
    output_dir = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / "entry.txt"
    output_file.write_text(ENTRY_TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
