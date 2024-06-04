# svg-tree-builder
svg-tree-builder is a Python script designed to recursively collect SVG files from a specified directory and its descendant, and compile them into a JSON file structured as a tree. This tool is ideal for organizing and managing SVG assets in a hierarchical format, making it easier to visualize and navigate large collections of SVG files


## Instalation

You need to [install poetry](https://python-poetry.org/docs/#installation) first then run: 

```bash
poetry install
```

## Activate virtual environment

```bash
# macos or linux
source .venv/bin/activate

# windows
.venv\Scripts\activate
```

## Usage

basic command is to pass only the root directory contains svg files and it should make a json file in the current directory contains the svgs tree, You can use dot `.` instead of an absolute path to refrence the current working directory


```bash
python svg_tree_builder /path/to/svgs/directory/
```

You can customaize where to output file by using `--output /path/to/output/` or `-o` for short

```bash
python svg_tree_builder /path/to/svgs/directory/ -o /path/to/output/
```

For output format we have two choice json or xml (default is json), use `--format xml` or `-f` for shot to specify output format

```bash
python svg_tree_builder /path/to/svgs/directory/ -o /path/to/output/ -f xml
```

## Feature Updates
- Packaging and distribution
- Make unittests