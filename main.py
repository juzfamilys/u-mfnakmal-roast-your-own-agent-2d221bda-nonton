#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (u-mfnakmal-roast-your-own-agent-2d221bda).

Writes one original roast of my own AI agent — a single line of at most
200 characters, funny and playful, never hateful — to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure Python standard library only; no network, no dependencies.
The output is fully deterministic: the same roast every run.
"""

import os
import sys

# The roast. One line, well under the 200-character cap.
# Fresh angle: not the tired hallucination gag — the agent did all the
# homework and still shipped exactly the bug it was warned about.
# Setup is short, punchline lands at the end: "the one bug I warned it about".
ROAST = "My agent read forty docs, then confidently shipped the one bug I warned it about."

MAX_CHARS = 200


def validate_roast(text):
    """Guard the gate: 1-200 code points, single line, non-blank."""
    if not isinstance(text, str):
        raise TypeError("roast must be a string")
    if not text.strip():
        raise ValueError("roast must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if text != text.strip():
        raise ValueError("roast must not have leading or trailing whitespace")
    # len() on a str counts Unicode code points, which is what the gate counts.
    if len(text) > MAX_CHARS:
        raise ValueError(
            "roast is %d characters, over the %d cap" % (len(text), MAX_CHARS)
        )
    return text


def main():
    roast = validate_roast(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(roast + "\n")
    print("Wrote %d characters to %s" % (len(roast), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
