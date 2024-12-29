import os
import tempfile
from folder2prompt_cli.main import process_directory, format_repo_contents


def test_process_single_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file = os.path.join(tmpdir, "test.txt")
        with open(test_file, "w") as f:
            f.write("test content")
        
        contents = process_directory(
            tmpdir,
            exclude_patterns=[],
            exclude_recursive_patterns=[],
            all_files=True
        )
        
        assert len(contents) == 1
        assert contents[0]["path"] == "test.txt"
        assert contents[0]["content"] == "test content" 