import os.path
import pytest

import solutions.day_13

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_13.txt')


@pytest.fixture
def test_data():
    return solutions.day_13.read_paper(TEST_FILE)

def test_part_1(test_data):
    grid, folds = test_data
    assert solutions.day_13.part_1(grid, folds) == 17

def test_part_2(test_data):
    grid, folds = test_data
    expected = {
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
        (1, 4),
        (2, 4),
        (3, 4),
    }
    solutions.day_13.part_2(grid, folds)
    assert set(grid.keys()) == expected
