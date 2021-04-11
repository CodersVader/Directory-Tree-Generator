from pathlib import Path
import argparse
import tree

# Parse CLI Arguments
parser = argparse.ArgumentParser(description='Process path.')
parser.add_argument(dest='path')
parser.add_argument('-f', '--file', dest='file', type=bool, default=False,
                    help="Save to file or not. Default is display to CLI.")

root = Path(parser.parse_args().path)
file_or_cli = parser.parse_args().file

# Create instance of Tree class and generate the directory structure.
creator = tree.Tree(root)
creator.tree_generator()

# By default print generated structure to CLI else save it to text file.
if file_or_cli:
    creator.to_file()
else:
    creator.to_cli()