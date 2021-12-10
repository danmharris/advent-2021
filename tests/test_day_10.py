import os.path
import pytest

import solutions.day_10
from utils.io import read_strings

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_10.txt')


@pytest.fixture
def test_data():
    return read_strings(TEST_FILE)

def test_part_1(test_data):
    assert solutions.day_10.part_1(test_data) == 26397

def test_part_2(test_data):
    assert solutions.day_10.part_2(test_data) == 288957
