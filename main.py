#!/usr/bin/env python3
"""Snooze Button Roast — writes one roast line to entry.txt.

The entry roasts an alarm clock that rings at 6 AM on a Saturday.
The program writes exactly one line, well under the 200-character gate.
"""
import os

ENTRY = (
    "My alarm clock rang at 6 AM on a Saturday like a tiny manager "
    "with no life, no weekend, and a grudge against mine."
)

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
