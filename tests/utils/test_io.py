import pytest
from utils.io import read_ints, read_actions


@pytest.fixture
def input_file(tmp_path):
    return tmp_path / "input"

def test_read_ints(input_file):
    input_file.write_text("1\n2\n3\n4\n")
    expected = [1, 2, 3, 4]
    assert read_ints(str(input_file)) == expected

def test_read_actions(input_file):
    input_file.write_text("up 1\ndown 2\nleft 3\n")
    expected = [
        ("up", 1),
        ("down", 2),
        ("left", 3),
    ]
    assert read_actions(str(input_file)) == expected
