import os.path
import pytest

import solutions.day_05

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_05.txt')


@pytest.fixture
def test_file():
    with open(TEST_FILE, 'r') as f:
        yield f


@pytest.fixture
def test_lines():
    return solutions.day_05.read_lines(TEST_FILE)

def test_part_1(test_lines):
    assert solutions.day_05.part_1(test_lines) == 5

def test_part_2(test_lines):
    assert solutions.day_05.part_2(test_lines) == 12
