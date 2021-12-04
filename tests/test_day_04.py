import os.path
import pytest

import solutions.day_04

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_04.txt')


@pytest.fixture
def test_file():
    with open(TEST_FILE, 'r') as f:
        yield f


@pytest.fixture
def test_boards():
    return solutions.day_04.read_bingo(TEST_FILE)

def test_part_1(test_boards):
    numbers, boards = test_boards
    assert solutions.day_04.part_1(numbers, boards) == 4512

def test_part_2(test_boards):
    numbers, boards = test_boards
    assert solutions.day_04.part_2(numbers, boards) == 1924
