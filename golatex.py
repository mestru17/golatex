#!/usr/bin/env python3

import argparse

from pygments import highlight
from pygments.filters import VisibleWhitespaceFilter
from pygments.formatters import LatexFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer_for_filename
from pygments.util import ClassNotFound

from styles.onehalf import OneHalfLightStyle


def get_style_by_name(name: str):
    if name == "onehalf":
        return OneHalfLightStyle
    raise ClassNotFound(f"No style matching name '{name}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="golatex")
    parser.add_argument("file", type=str)
    parser.add_argument("-p", "--preamble", action="store_true")
    parser.add_argument("-l", "--language", type=str, default=None)
    parser.add_argument("-s", "--style", type=str, default="onehalf")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        code = f.read()

    lexer = (
        get_lexer_by_name(args.language)
        if args.language
        else guess_lexer_for_filename(args.file, code)
    )

    # lexer = get_lexer_by_name(args.language)
    lexer.add_filter(VisibleWhitespaceFilter(tabs=" ", tabsize=2))

    style = get_style_by_name(args.style)

    formatter = LatexFormatter(style=style)
    if args.preamble:
        print("% =========================")
        print("% Put this in your preamble")
        print("% =========================")
        print(formatter.get_style_defs().strip())
        print("----------------------------------------------------------------\n")

    try:
        with open(args.file, "r") as f:
            print(highlight(f.read(), lexer, formatter).strip())
    except IOError as e:
        print(f"Error reading file '{args.file}': {e}")
