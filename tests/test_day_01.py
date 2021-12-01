from solutions import day_01

TEST_DATA = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def test_part_one():
    assert day_01.part_1(TEST_DATA) == 7

def test_part_two():
    assert day_01.part_2(TEST_DATA) == 5
