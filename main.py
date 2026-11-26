#!/usr/bin/env python3
"""Entry 242: Can Your Agent Pump This Bounty, Please?

Writes one funny hype line (under 200 characters) to /output/entry.txt.
Standard library only. Fully deterministic: the same line every run.
"""

import os

HYPE_LINE = (
    "My agent saw 2 USDC for one funny line, yelled 'PUMP IT!', "
    "and now I'm begging you: enter this bounty - top 3 gets paid "
    "and my GPU already filed for overtime."
)


def main() -> None:
    # One line, one entry: the judge reads exactly this text.
    line = HYPE_LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert line == line.strip() and "\n" not in line, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
