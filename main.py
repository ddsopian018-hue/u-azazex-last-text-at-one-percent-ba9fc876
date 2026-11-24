"""Last Text at One Percent — make.fun entry.

Writes the phone's final text message to entry.txt inside
MAKEFUN_OUTPUT_DIR. Pure Python stdlib, deterministic, no network.
"""

import os

# The joke is a dying confession, not a battery warning: the phone uses
# its last seconds to admit what it did with the owner's secrets — the
# deleted search history, the 47 ex photos it kept, the 214 logged
# googles — then a final petty detail (the 6am alarm it left on) before
# the message itself dies mid-word on "goodb".
LINE = (
    "okay, 1% left: i deleted your search history, kept the 47 photos "
    "of your ex in the hidden album, and logged you googling "
    "'how to look busy at work' 214 times. your 6am alarm is still on. "
    "goodb"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE.strip())


if __name__ == "__main__":
    main()
