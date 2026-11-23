#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one roast line to /output/entry.txt.
"""

import os
import sys

LINE = "It writes, grades, revises, publishes, submits — I approve. I'm not a developer, I'm a rubber stamp with a wallet password."


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        print(f"error: entry is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
