import solutions.day_07

TEST_DATA = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_part_1():
    assert solutions.day_07.part_1(TEST_DATA) == 37

def test_part_2():
    assert solutions.day_07.part_2(TEST_DATA) == 168
