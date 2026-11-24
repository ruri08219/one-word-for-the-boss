"""One word for the boss.

Writes exactly one word describing the boss to /output/entry.txt.
The word has to land on its own: no phrase, no caption, no explanation.
"""

import os

WORD = "goalpost"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    text = WORD + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == text, "round-trip mismatch: %r != %r" % (back, text)


if __name__ == "__main__":
    main()
