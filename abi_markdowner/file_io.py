# file_io.py

import json

def save_markdown_to_file(markdown_content, file_path):
    """Save the generated Markdown to a file."""
    with open(file_path, 'w') as file:
        file.write(markdown_content)

def read_abi_from_file(file_path):
    """Read ABI data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)
