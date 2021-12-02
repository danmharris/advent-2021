from solutions import day_02

TEST_DATA = [
    ('forward', 5),
    ('down', 5),
    ('forward', 8),
    ('up', 3),
    ('down', 8),
    ('forward', 2),
]

def test_part_1():
    assert day_02.part_1(TEST_DATA) == 150

def test_part_2():
    assert day_02.part_2(TEST_DATA) == 900
