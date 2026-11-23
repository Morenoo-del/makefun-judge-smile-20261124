"""Make the Judge Smile — entry program.

Writes one line, at most 200 characters, about a small good thing
that happened today, to /output/entry.txt.
"""

import os

LINE = (
    "At 6:40 this morning the rain stopped the second I reached my door, "
    "and a stray cat I'd never met walked me the last ten steps home, "
    "tail up like it owned the street."
)


def main() -> None:
    # The line is a single sentence about one small good thing today:
    # rain stopping at the door, and a stray cat escorting me home.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
