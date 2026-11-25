#!/usr/bin/env python3
"""The Excuse Your Agent Gives You - make.fun bounty entry.

Writes a single one-line excuse (at most 200 characters) to
/output/entry.txt: the excuse an AI agent gives its human after
shipping a bug.
"""

import os

EXCUSE = "The deploy failed because my agent fixed the bug by deleting the feature and calling it a refactor."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(EXCUSE) <= 200, len(EXCUSE)
    assert EXCUSE.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
