import os.path
import pytest

import solutions.day_18

TEST_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day_18.txt')


@pytest.fixture
def test_data():
    return solutions.day_18.read_numbers(TEST_FILE)


def test_add():
    node_1 = solutions.day_18.Node.parse('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
    node_2 = solutions.day_18.Node.parse('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')

    sfn_1 = solutions.day_18.SnailfishNumber(node_1)
    sfn_2 = solutions.day_18.SnailfishNumber(node_2)
    sfn_1.add(sfn_2)

    assert str(sfn_1.root) == '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'

def test_copy():
    node = solutions.day_18.Node.parse('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    new_node = node.copy()
    assert str(node) == str(new_node)

def test_depth():
    node = solutions.day_18.Node.parse('[[[[[9,8],1],2],3],4]')
    assert node.left.left.left.left.left.value == 9
    assert node.left.left.left.left.left.depth() == 5

def test_explode():
    node = solutions.day_18.Node.parse('[[[[[9,8],1],2],3],4]')
    node.left.left.left.left.explode()
    assert str(node) == '[[[[0,9],2],3],4]'

def test_magnitude():
    node = solutions.day_18.Node.parse('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    assert node.magnitude() == 1384


@pytest.mark.parametrize('number', [
    '[1,2]',
    '[[1,2],3]',
    '[9,[8,7]]',
    '[[1,9],[8,5]]',
    '[[[[1,2],[3,4]],[[5,6],[7,8]]],9]',
    '[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]',
    '[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]',
])
def test_parse(number):
    assert str(solutions.day_18.Node.parse(number)) == number

def test_reduce():
    node = solutions.day_18.Node.parse('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
    sfn = solutions.day_18.SnailfishNumber(node)
    sfn.reduce()
    assert str(sfn.root) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

def test_part_1(test_data):
    assert solutions.day_18.part_1(test_data) == 4140

def test_part_2(test_data):
    assert solutions.day_18.part_2(test_data) == 3993
