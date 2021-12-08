import os.path
import pytest

import solutions.day_08

TEST_DATA = [
 (['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'],['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])
]
TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_08.txt')


@pytest.fixture
def test_patterns():
    return solutions.day_08.read_patterns(TEST_FILE)

def test_part_1(test_patterns):
    assert solutions.day_08.part_1(test_patterns) == 26

def test_part_2(test_patterns):
    assert solutions.day_08.part_2(TEST_DATA) == 5353
    assert solutions.day_08.part_2(test_patterns) == 61229
