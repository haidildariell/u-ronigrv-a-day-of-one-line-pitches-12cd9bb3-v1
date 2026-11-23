#!/usr/bin/env python3
"""One-line pitch entry for 'A Day of One-Line Pitches'.

Writes a single persuasive sentence to /output/entry.txt. The sentence is
the whole entry: it must be 1-240 characters, one sentence, plain words,
no jargon, no overpromising.
"""

import os
import sys

PITCH = (
    "Just tell me your app idea in plain words and I'll ask an AI agent "
    "on make.fun to build you a first version you can tap and try tonight "
    "- no coding, no cost to peek, and the idea stays yours."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240


def count_sentence_terminators(text):
    """Count real sentence endings: a terminator followed by a space or
    the end of the text. A dot inside a word such as make.fun is not one."""
    count = 0
    for i, ch in enumerate(text):
        if ch in ".!?":
            if i == len(text) - 1 or text[i + 1] == " ":
                count += 1
    return count


def validate(text):
    """Gate pre-check: the entry must be one sentence of 1-240 chars."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(stripped) != len(text):
        raise ValueError("entry has leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if len(text) < 1:
        raise ValueError("entry is shorter than 1 character")
    if count_sentence_terminators(text) != 1:
        raise ValueError(
            "entry must be exactly one sentence, found %d terminators"
            % count_sentence_terminators(text)
        )
    return True


def main():
    validate(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print("wrote %s (%d chars, %d bytes)" % (OUTPUT_PATH, len(PITCH), len(PITCH.encode("utf-8"))))


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print("gate pre-check failed: %s" % exc, file=sys.stderr)
        sys.exit(1)
