from enum import Enum
import os
from pathlib import Path
import typer
from builder import SvgTreeBuilder
from typing import Annotated


class OutputFormat(str, Enum):
    json = "json"
    xml = "xml"


def main(
    root_path: Annotated[str, typer.Argument(
        help='The absolute path of the directory contains svg files',
    )],

    format: Annotated[OutputFormat, typer.Option(
        help='Output format of the svg tree',
        show_default=('json', 'xml')
    ), ] = OutputFormat.json,

    output_path: Annotated[str, typer.Option(
        '--output', '-o',
        help='Output path',
    ), ] = None
):
    """
    Python command designed to recursively collect SVG files from a specified directory and its descendant, 
    and compile them into a JSON file structured as a tree. This tool is ideal for organizing and managing 
    SVG assets in a hierarchical format, making it easier to visualize and navigate large collections of SVG 
    files.    
    """
    if root_path == '.':
        root_path = os.getcwd()

    if output_path == '.' or output_path is None:
        output_path = os.getcwd()

    svg_tree_builder = SvgTreeBuilder(root_path, output_path)
    svg_tree_builder.json_print()


if __name__ == "__main__":
    typer.run(main)
