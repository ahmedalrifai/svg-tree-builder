from builder import SvgTreeBuilder


def main():
    root_path = '/Users/ahmedalrifai/Downloads/SVG Folder Testing for Ahmed'
    print(f'Root Path: {root_path}')
    svg_tree_builder = SvgTreeBuilder(root_path)
    svg_tree_builder.pretty_print()


if __name__ == "__main__":
    main()
