from pygments.style import Style
from pygments.token import (
    Text,
    Operator,
    Punctuation,
    Comment,
    Keyword,
    Number,
    String,
    Name,
)

class OneHalfLightStyle(Style):
    black = "#383a42"
    red = "#e45649"
    green = "#50a14f"
    yellow = "#c18401"
    blue = "#0184bc"
    magenta = "#a626a4"
    cyan = "#0997b3"
    white = "#fafafa"
    fg = "#383a42"
    bg = "#fafafa"
    comment = "#a0a1a7"

    default_style = ""
    styles = {
        Text: fg,
        Operator: cyan,
        Punctuation: red,
        Comment: comment,
        Comment.Single: comment,
        Comment.Multiline: comment,
        Keyword: blue,
        Keyword.Constant: yellow,
        Keyword.Declaration: blue,
        Keyword.Namespace: blue,
        Keyword.Type: blue,
        Number: magenta,
        Number.Float: magenta,
        Number.Oct: magenta,
        Number.Hex: magenta,
        Number.Integer: magenta,
        String: green,
        String.Char: green,
        Name.Builtin: yellow,
        Name.Other: fg,
    }
