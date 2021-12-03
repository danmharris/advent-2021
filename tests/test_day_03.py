from solutions import day_03

TEST_DATA = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

def test_part_1():
    assert day_03.part_1(TEST_DATA) == 198

def test_part_2():
    assert day_03.part_2(TEST_DATA) == 230
