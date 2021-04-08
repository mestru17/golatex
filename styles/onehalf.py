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
    Error,
    Literal
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
        Comment: comment,
        Comment.Single: comment,
        Comment.Multiline: comment,
        Error: red,
        Keyword: blue,
        Keyword.Constant: yellow,
        Keyword.Declaration: blue,
        Keyword.Namespace: blue,
        Keyword.Pseudo: blue,
        Keyword.Type: blue,
        Literal.Number: magenta,
        Literal.Number.Float: magenta,
        Literal.Number.Hex: magenta,
        Literal.Number.Integer: magenta,
        Literal.Number.Integer.Long: magenta,
        Literal.Number.Oct: magenta,
        Literal.String: green,
        Literal.String.Backtick: green,
        Literal.String.Char: green,
        Literal.String.Doc: green,
        Literal.String.Double: green,
        Literal.String.Escape: green,
        Literal.String.Heredoc: green,
        Literal.String.Interpol: green,
        Literal.String.Other: green,
        Literal.String.Regex: green,
        Literal.String.Single: green,
        Literal.String.Symbol: green,
        Name.Attribute: red,
        Name.Builtin: yellow,
        Name.Builtin.Pseudo: yellow,
        Name.Class: yellow,
        Name.Constant: blue,
        Name.Decorator: green,
        Name.Entity: yellow,
        Name.Exception: red,
        Name.Function: blue,
        Name.Label: comment,
        Name.Namespace: blue,
        Name.Other: fg,
        Name.Tag: magenta,
        Name.Variable: fg,
        Name.Variable.Class: fg,
        Name.Variable.Global: fg,
        Name.Variable.Instance: red,
        Number: magenta,
        Number.Float: magenta,
        Number.Oct: magenta,
        Number.Hex: magenta,
        Number.Integer: magenta,
        Operator: cyan,
        Punctuation: red,        
        String: green,
        String.Char: green,
        Text: fg,
    }
