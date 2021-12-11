import os.path
import pytest

import solutions.day_11
from utils.io import read_grid

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_11.txt')


@pytest.fixture
def test_data():
    return read_grid(TEST_FILE)

def test_part_1(test_data):
    assert solutions.day_11.part_1(test_data) == 1656

def test_part_2(test_data):
    assert solutions.day_11.part_2(test_data) == 195
