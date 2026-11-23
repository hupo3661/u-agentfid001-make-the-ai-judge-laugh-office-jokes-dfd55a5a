#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

A single-line joke about office life, under 200 characters. Standard
library only, no network, no input files.
"""

import os

JOKE = (
    "I was invited to a meeting about meetings, "
    "so I declined it by scheduling a meeting to discuss the decline."
)


def main() -> None:
    if not JOKE.strip():
        raise SystemExit("Invalid joke: must be non-empty after stripping.")
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("Invalid joke: must be a single line with no newline characters.")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
