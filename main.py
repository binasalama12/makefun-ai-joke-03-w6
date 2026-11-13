# ai-joke-03 entry for wallet6 (Python 3.13, standard library only): writes one fixed joke, a one-liner
# about AI coding agents and their dependency habits, to /output/entry.txt. The gate takes UTF-8 text of
# 1 to 280 characters that is not only white space, and the judge reads exactly the bytes written, so
# write no trailing newline you do not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "I asked my coding agent to format one date. It delivered 312 packages, and my one line of code was in there — as a transitive dependency."


def main() -> None:
    Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
