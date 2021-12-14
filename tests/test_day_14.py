import os.path
import pytest

import solutions.day_14

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_14.txt')


@pytest.fixture
def test_data():
    return solutions.day_14.read_polymer_template(TEST_FILE)

def test_part_1(test_data):
    template, rules = test_data
    assert solutions.day_14.part_1(template, rules) == 1588

def test_part_2(test_data):
    template, rules = test_data
    assert solutions.day_14.part_2(template, rules) == 2188189693529
