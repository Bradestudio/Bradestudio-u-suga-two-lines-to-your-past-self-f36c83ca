"""Two Lines to Your Past Self — make.fun bounty entry.

Writes two lines (266 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

Line one warns the past self about one specific moment: sliding a
resignation letter across Mr. Hart's desk on Monday 3 June 2019 at
9 a.m. — and says wait one week. Line two traces the cause and
effect: seven days later the firm announced redundancy payouts, so
waiting turned a clean exit into six months' pay that funded the
first year working for yourself. A real date, a real desk, a real
decision — and a concrete change that followed from it.
"""

import os
import sys

ENTRY = (
    "Don't slide that resignation letter across Mr. Hart's desk on "
    "Monday 3 June 2019 at 9 a.m. \u2014 wait one week.\n"
    "Seven days later the firm announced redundancy payouts, and "
    "waiting turned a clean exit into six months' pay that funded "
    "your first year working for yourself."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    lines = text.split("\n")
    if len(lines) != 2:
        sys.exit("entry must be exactly two lines, got %d" % len(lines))
    for line in lines:
        if not line.strip():
            sys.exit("entry line must not be blank")
        if line != line.strip():
            sys.exit("entry line must not start or end with whitespace")
    if not 1 <= len(text) <= 280:
        sys.exit("entry must be 1-280 characters, got %d" % len(text))
    if not lines[0].endswith("wait one week."):
        sys.exit("line one must end with the warning to wait one week")
    if not lines[1].endswith("working for yourself."):
        sys.exit("line two must end with the concrete change")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, %d lines)"
          % (path, len(text), len(data), len(lines)))


if __name__ == "__main__":
    main()
