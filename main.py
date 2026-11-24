"""One Line of Earned Pride.

Writes one line (119 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

# Revision note: length gate checked against the kit's 1-240 range, verified
# from the bounty page (one line, 1 to 240 characters, to /output/entry.txt).
# The single-line check below was added in revision so a stray newline in
# the entry can never slip through silently.
LINE = "Fixed the bug at 2am, shipped before sunrise, and the dashboard I built from nothing now runs the whole team's morning."


# Bounty gate: the entry must be one line of 1-240 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 240


def main() -> None:
    if not MIN_CHARS <= len(LINE) <= MAX_CHARS:
        print(
            f"entry length {len(LINE)} chars outside {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
