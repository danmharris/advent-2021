import os.path
import pytest

import solutions.day_15
from utils.io import read_grid

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_15.txt')


@pytest.fixture
def test_data():
    return read_grid(TEST_FILE)

def test_part_1(test_data):
    assert solutions.day_15.part_1(test_data) == 40

def test_part_2(test_data):
    assert solutions.day_15.part_2(test_data) == 315
