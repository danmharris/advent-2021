import solutions.day_17

def test_fire():
    assert solutions.day_17.fire(7, 2, (20, 30), (-10, -5)) is True
    assert solutions.day_17.fire(6, 3, (20, 30), (-10, -5)) is True
    assert solutions.day_17.fire(9, 0, (20, 30), (-10, -5)) is True
    assert solutions.day_17.fire(17, -4, (20, 30), (-10, -5)) is False

def test_part_1():
    assert solutions.day_17.part_1((20, 30), (-10, -5)) == 45

def test_part_2():
    assert solutions.day_17.part_2((20, 30), (-10, -5)) == 112
