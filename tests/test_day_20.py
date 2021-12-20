import os.path
import pytest

import solutions.day_20

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_20.txt')


@pytest.fixture
def test_data():
    return solutions.day_20.read_image(TEST_FILE)

def test_part_1(test_data):
    enhance, image = test_data
    assert solutions.day_20.part_1(enhance, image) == 35

def test_part_2(test_data):
    enhance, image = test_data
    assert solutions.day_20.part_2(enhance, image) == 3351
