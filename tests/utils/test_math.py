from utils.math import transpose, hex_to_bin

def test_transpose():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose(data) == expected

def test_hex_to_bin():
    expected = '110100101111111000101000'
    assert hex_to_bin('D2FE28') == expected
