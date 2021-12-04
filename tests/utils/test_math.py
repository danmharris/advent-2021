from utils.math import transpose

def test_transpose():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose(data) == expected
