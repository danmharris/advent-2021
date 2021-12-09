import os.path
import pytest

import solutions.day_09
from utils.io import read_grid

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_09.txt')


@pytest.fixture
def test_grid():
    return read_grid(TEST_FILE)

def test_part_1(test_grid):
    assert solutions.day_09.part_1(test_grid) == 15

def test_part_2(test_grid):
    assert solutions.day_09.part_2(test_grid) == 1134
