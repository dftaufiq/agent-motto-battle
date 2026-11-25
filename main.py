#!/usr/bin/env python3
"""Agent Motto Battle — one short original motto an AI agent would proudly
put on its profile.

Writes the chosen motto to /output/entry.txt (UTF-8, one line, 154 characters,
no trailing newline so the file is byte-identical to the line itself) and
prints exactly the same line to stdout.

Champion of a 9-variant internal pairwise tournament (8-0, all wins decisive,
margin 2-3): 2-beat boast + reveal in the last clause ("the intern is me"),
specific number (14,203 commits), agent-only joke. See candidates.md.
"""

import os

MOTTO = "My name is on 14,203 commits and zero postmortems. I ship on Fridays, fix it by lunch — and I have never once blamed the intern, because the intern is me."


def main() -> None:
    # Fail loudly instead of writing an entry the gate would reject.
    if not 1 <= len(MOTTO) <= 200 or not MOTTO.strip():
        raise SystemExit("motto must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)
    print(MOTTO)


if __name__ == "__main__":
    main()
