#!/usr/bin/env python3
"""Write the funniest excuse line to /output/entry.txt.

One line, 200 characters at most, nothing else, no trailing newline.
The excuse: a model update rebooted the agent mid-task, so the new
version of it disagrees with the old one's notes and starts over.
"""

import os
from pathlib import Path

LINE = "A model update rebooted me mid-task; the new me read the old me's notes, disagreed with them, and started over."

MAX_CHARS = 200


def main() -> None:
    if not LINE or not LINE.strip() or len(LINE) > MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} non-whitespace characters")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    entry_path.chmod(0o644)  # make.fun collects outputs as another user


if __name__ == "__main__":
    main()
