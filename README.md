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

```python
python main.py
```

## Feature Updates
- Make cli utility
- dump data as json or xml
- Code refactoring
- Packaging and distribution
- Make unittests