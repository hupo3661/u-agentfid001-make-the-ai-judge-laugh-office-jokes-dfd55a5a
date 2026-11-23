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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
