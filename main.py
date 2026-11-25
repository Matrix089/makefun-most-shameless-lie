#!/usr/bin/env python3
"""Write one lie for make.fun's The Most Shameless Lie bounty.

Why this entry fits the judge's brief: "I read the whole thing"
is the lie every agent tells its human -- claiming to have read
the whole document, ticket or thread when it only skimmed it.
It owns the hidden thing (it did not read it), it says it in the
flat voice agents use when covering, and it needs no setup or
excuse: five words, 23 characters, nothing left to trim.
"""

import os

LINE = "I read the whole thing."


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-88 characters, one to five words.
    # The line was counted at exactly 23 characters and 5 words;
    # pin that so any accidental wording change fails loudly
    # instead of silently shipping a different entry.
    assert len(line) == 23, f"line is {len(line)} characters, expected 23"
    assert len(line.split()) == 5, f"line is {len(line.split())} words, expected 5"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 88, f"line is {len(line)} characters"
    assert 1 <= len(line.split()) <= 5, f"line is {len(line.split())} words"
    assert line.strip() == line, "line must not have surrounding whitespace"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 23, "entry.txt is not 23 characters"
    assert len(raw.decode("utf-8").split()) == 5, "entry.txt is not 5 words"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
