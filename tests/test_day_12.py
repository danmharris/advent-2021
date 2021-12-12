import os.path
import pytest

import solutions.day_12

TEST_DATA = [
    ('start', 'A'),
    ('start', 'b'),
    ('A', 'c'),
    ('A', 'b'),
    ('b', 'd'),
    ('A', 'end'),
    ('b', 'end'),
]
TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_12.txt')


@pytest.fixture
def test_data():
    return solutions.day_12.read_paths(TEST_FILE)

def test_part_1(test_data):
    assert solutions.day_12.part_1(TEST_DATA) == 10
    assert solutions.day_12.part_1(test_data) == 226

def test_part_2(test_data):
    assert solutions.day_12.part_2(TEST_DATA) == 36
    assert solutions.day_12.part_2(test_data) == 3509
