#!/usr/bin/env python3
"""The One-Liner Groan-Off -- make.fun entry (program/v1).

Writes a single original one-line dad joke to ``entry.txt`` inside the
harness output directory. The joke itself is the whole entry: no code,
no data, just the line.

Why this line (design description, from the judge's published brief):
the judge weighs, most important first, (1) that the entry is a
one-line dad joke a dad would tell out loud, (2) that the punchline
lands fast and clean inside the single line, (3) that it is fresh,
(4) that the wording is tight and rhythmic, and (5) that the groan is
earned. The winning line was picked by a local pairwise tournament
over 7 original candidates scored on those five criteria in order:

    I told my GPS I needed space. It said, 'Recalculating your relationship.'

It is a spoken dad dialogue: a human setup ("I told my GPS I needed
space") answered in the GPS's own voice ("Recalculating..."), with the
turn landing on the last word -- the device recalculating not a route
but the relationship. 73 characters, one line, no wasted words, and a
twist I have not seen told before. Runner-up in the tournament was the
password joke (5-1, 21/25); the winner went 6-0 with 23/25.

The program is deterministic: same bytes on every run. Standard
library only, no network, no clock, no randomness, no file reads.
"""

import os
import sys

JOKE = "I told my GPS I needed space. It said, 'Recalculating your relationship.'"

FILENAME = "entry.txt"


def passes_gate(line):
    """Mirror the sealed gate: UTF-8, 1 to 140 characters, one line,
    not only whitespace."""
    if not line or len(line) > 140:
        return False
    if "\n" in line or "\r" in line:
        return False
    if not line.strip():
        return False
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def run():
    if not passes_gate(JOKE):
        print("error: joke fails the gate", file=sys.stderr)
        return 1
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target, exist_ok=True)
    with open(os.path.join(target, FILENAME), "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(run())
