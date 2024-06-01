import json
from pathlib import Path


class SvgTreeBuilder:
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        self.current_path = Path(root_path)
        self.svg_tree = self.build_svg_tree()

    @property
    def is_root(self):
        return self.current_path == self.root_path

    def collect_svg_content(self, svg_file: Path) -> dict:
        svg_content = svg_file.read_text()

        return {
            'name': svg_file.name,
            'content': svg_content
        }

    def collect_svgs(self):
        svg_files = list(self.current_path.glob('*.svg'))
        svgs_data = sorted([self.collect_svg_content(svg_file)
                            for svg_file in svg_files], key=lambda icon: icon['name'])

        return svgs_data

    def build_groups(self, svg_tree={}):
        sub_folders = list(sorted([
            sub_folder for sub_folder in self.current_path.iterdir() if sub_folder.is_dir()], key=lambda sub_folder: sub_folder.name))

        for i, sub_folder in enumerate(sub_folders):
            self.current_path = sub_folder
            svg_tree['groups'].append({
                'name': self.current_path.name,
                'svgs': [],
                'groups': [],
            })
            self.build_svg_tree(svg_tree['groups'][i])

        return svg_tree['groups']

    def build_svg_tree(self, svg_tree={}) -> dict:
        if self.is_root:
            svg_tree = {
                'name': self.root_path.name,
                'svgs': [],
                'groups': [],
            }

        svg_tree['svgs'] = self.collect_svgs()
        svg_tree['groups'] = self.build_groups(svg_tree)

        return svg_tree

    def pretty_print(self):
        print('<start')

        print(self.svg_tree)
        print('end>')
