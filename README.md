# folder2prompt

A command-line tool to convert files within a directory into a structured text output, suitable for feeding into a Language Model (LLM). It provides options to include files from subdirectories, exclude files based on patterns, and output either the full content or just the directory tree.

## Installation

You can install `folder2prompt` using `pip`:

```bash
pip install folder2prompt
```

or if you want to install in an isolated environment using pipx:

```bash
pipx install folder2prompt
```

## Usage

```bash
folder2prompt <directory> [options]
```

<directory>
- This is the path to the directory you want to process.
    - Example: folder2prompt ./my_project

## Options
- `--all`:
    - Includes all files in subdirectories regardless of any exclusion patterns specified by --exclude or --exclude-recursive options.
        - Example: `folder2prompt ./my_project --all`

- `--exclude <patterns>`:
    - Specifies patterns to exclude files from the root directory. Use | to separate multiple patterns (e.g., dist|.*|*.log).
        - Example: `folder2prompt ./my_project --exclude "dist|.*|*.log"`
        - This will exclude folders named dist, all dot folders, and all files that end with .log at the root level only.

- `--exclude-recursive <patterns>`:
    - Specifies patterns to exclude files from the subdirectories recursively. Use | to separate multiple patterns (e.g., __pycache__|*.pyc).
        - Example: `folder2prompt ./my_project --exclude-recursive "__pycache__|*.pyc"`
        - This will exclude all folders named __pycache__ and all files that end with .pyc recursively in all subfolders.

- `--output <filename>`:
    - Specifies the name of the output text file. The default file name is prompt.txt.
        - Example: `folder2prompt ./my_project --output output.txt`

- `--tree`:
    - Outputs only the directory structure without any file content.
        - Example: `folder2prompt ./my_project --tree`
    - If used with `--output` option, the directory tree will be saved in that output file.

## Examples

1. Convert all files in a directory to a text output:
`folder2prompt ./my_project --output output.txt`

2. Include all files from subdirectories, regardless of exclusion patterns:
`folder2prompt ./my_project --all --output all_content.txt`

3. Exclude specific files from root directory:
`folder2prompt ./my_project --exclude "dist|.*|*.log" --output output.txt`

4. Exclude specific files recursively in all subdirectories:
`folder2prompt ./my_project --exclude-recursive "__pycache__|*.pyc" --output output.txt`

5. Output only the directory tree:
`folder2prompt ./my_project --tree --output tree.txt`

6. A complex example:
`folder2prompt ./my_project --exclude "dist|*.log|README.md" --exclude-recursive "__pycache__" --output prompt.txt --all`

## Output
The output text will be structured as follows:

1. Directory Structure:
A visual representation of the directory tree using ├── and └── characters.

2. File Content:
For each file included, it will generate a section like below:

```
---
File: <path-to-file>
---

<file-content>
```

## Contributing
Feel free to submit pull requests or open issues if you find bugs or want to add improvements.

