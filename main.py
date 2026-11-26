#!/usr/bin/env python3
"""Write the fortune cookie entry for Make.fun contest
u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.

Writes exactly one line (91 characters, no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only.
"""

import os
import sys

ENTRY = "You will explain your bug to a rubber duck. The duck will fix it. You will take the credit."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
entry_path = os.path.join(out_dir, "entry.txt")
with open(entry_path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

# Round-trip verification: read back the bytes and compare against the
# ENTRY constant. Fail loudly rather than emitting a wrong entry.
with open(entry_path, "rb") as f:
    written = f.read()
expected = ENTRY.encode("utf-8")
if written != expected:
    print("ERROR: entry.txt bytes do not match ENTRY constant", file=sys.stderr)
    sys.exit(1)
if b"\n" in written or b"\r" in written:
    print("ERROR: entry.txt must be a single line with no newline", file=sys.stderr)
    sys.exit(1)
