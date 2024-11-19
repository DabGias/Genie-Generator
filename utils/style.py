import os
from enum import Enum

import click


class SpecialChars(Enum):
    TL_CORNER = "┌"
    TR_CORNER = "┐"
    BL_CORNER = "└"
    BR_CORNER = "┘"

    V_LINE = "│"
    H_LINE = "─"

    L_INTERSECTION = "┤"
    R_INTERSECTION = "├"


terminal_cols: int = os.get_terminal_size().columns
terminal_rows: int = os.get_terminal_size().lines

def info_box_header(title: str, content_len: int = 0):
    click.echo(f"{SpecialChars.TL_CORNER.value}{SpecialChars.H_LINE.value} {title} {SpecialChars.H_LINE.value * (content_len - len(title) - 1)}{SpecialChars.TR_CORNER.value}")

def info_box_row(content: str):
    click.echo(f"{SpecialChars.V_LINE.value} {content} {SpecialChars.V_LINE.value}")

def info_box_footer(content_len: int = 0):
    click.echo(f"{SpecialChars.BL_CORNER.value}{SpecialChars.H_LINE.value * (content_len + 2)}{SpecialChars.BR_CORNER.value}")

def info_box(title: str, content: str):
    info_box_header(title, len(content))
    info_box_row(content)
    info_box_footer(len(content))
