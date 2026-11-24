"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence about a small moment of wonder in everyday
life to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library.
"""

import os

ENTRY = (
    "The elevator mirror caught me mid-yawn, and for one floor "
    "I was a stranger politely pretending not to know me."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
