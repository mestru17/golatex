#!/usr/bin/env python3

import argparse

from pygments import highlight
from pygments.filters import VisibleWhitespaceFilter
from pygments.formatters import LatexFormatter
from pygments.lexers import GoLexer

from styles.onehalf import OneHalfLightStyle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="golatex")
    parser.add_argument("file", type=str)
    parser.add_argument("-p", "--preamble", action="store_true")
    args = parser.parse_args()

    lexer = GoLexer()
    lexer.add_filter(VisibleWhitespaceFilter(tabs=" ", tabsize=2))

    formatter = LatexFormatter(style=OneHalfLightStyle, linenos=True)
    if args.preamble:
        print("# =========================")
        print("# Put this in your preamble")
        print("# =========================")
        print(formatter.get_style_defs())
        print("----------------------------------------------------------------")

    try:
        with open(args.file, "r") as f:
            print(highlight(f.read(), lexer, formatter).strip())
    except IOError as e:
        print(f"Error reading file '{args.file}': {e}")
