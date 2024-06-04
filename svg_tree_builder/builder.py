import json
import xmltodict
from pathlib import Path

from rich import print


class SvgTreeBuilder:
    def __init__(self, root_path: str, output_path: str = None, file_format='json'):
        self.root_path = Path(root_path)
        self.current_path = Path(root_path)
        self.has_svgs = False

        self.output_path = Path(output_path)
        self.format = file_format
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

        if svg_files:
            self.has_svgs = True

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

    def save_to_file(self):
        if self.has_svgs:
            file_name = f'{self.root_path.name}.{self.format}'

            with open(self.output_path.joinpath(file_name), 'w') as fp:
                if self.format == 'json':
                    json.dump(self.svg_tree, fp, indent=2)
                elif self.format == 'xml':
                    xmltodict.unparse(
                        {'root': self.svg_tree}, fp, pretty=True)

                print(
                    f'Save output to "{self.output_path.joinpath(file_name)}"')
        else:
            print('Could not find svg files!')
