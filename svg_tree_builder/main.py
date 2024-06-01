import json

from pathlib import Path
from typing import List


def ccollect_svg_content(svg_file):
    return {
        'name': svg_file.name,
        'content': svg_file.read_text()
    }


def build_svg_tree(path: Path, svg_tree={}, is_root=True) -> List:
    if is_root:
        svg_tree = {
            'name': path.name,
            'icons': [],
            'groups': [],
        }

    sub_folders = sorted([
        sub_folder for sub_folder in path.iterdir() if sub_folder.is_dir()], key=lambda sub_folder: sub_folder.name)
    svg_files = path.glob('*.svg')

    svg_tree['icons'] = sorted([ccollect_svg_content(svg_file)
                               for svg_file in svg_files], key=lambda icon: icon['name'])

    for i, sub_folder in enumerate(sub_folders):
        svg_tree['groups'].append({
            'name': path.name,
            'icons': [],
            'groups': [],
        })
        build_svg_tree(sub_folder, svg_tree['groups'][i], False)

    return svg_tree


def main():
    root_path = Path(
        '/Users/ahmedalrifai/Downloads/SVG Folder Testing for Ahmed')
    print(f'Root Path: {root_path}')
    svg_tree = build_svg_tree(root_path)

    print(svg_tree)


if __name__ == "__main__":
    main()
