import math

class Node:
    @classmethod
    def parse(cls, number, parent=None):
        if number[0] != '[':
            return cls(parent, int(number[0]))
        node = cls(parent)
        stack = 0
        split_index = -1
        for index, char in enumerate(number):
            if char == '[':
                stack += 1
            elif char == ']':
                stack -= 1
            elif char == ',' and stack == 1:
                split_index = index
                break
        if split_index > -1:
            node.left = Node.parse(number[1:split_index], node)
            node.right = Node.parse(number[split_index+1:-1], node)
            return node

    def __init__(self, parent, value=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value

    def copy(self):
        new_node = Node(None)
        if self.is_leaf():
            new_node.value = self.value
        else:
            left = self.left.copy()
            left.parent = new_node
            new_node.left = left
            right = self.right.copy()
            right.parent = new_node
            new_node.right = right
        return new_node

    def depth(self):
        depth = 0
        root = self.parent
        while root is not None:
            depth += 1
            root = root.parent
        return depth

    def explode(self):
        if not (self.left.is_leaf() and self.right.is_leaf()):
            raise Exception('Explode cannot be performed on this node')

        """
        Idea here is that the next node on the left will be the next available
        left node as you go back up the tree (that isn't where we've just come
        from), and then from there keep going right. Flip this logic for the
        next node on the right.
        """
        prev_node = self
        node = self.parent
        right_node = None
        left_node = None
        while node is not None:
            right_movement = node.right == prev_node
            if right_movement:
                if left_node is None:
                    left_node = node.left
            elif right_node is None:
                right_node = node.right
            prev_node = node
            node = node.parent

        if left_node is not None:
            while not left_node.is_leaf():
                left_node = left_node.right
            left_node.value += self.left.value
        if right_node is not None:
            while not right_node.is_leaf():
                right_node = right_node.left
            right_node.value += self.right.value

        self.left = None
        self.right = None
        self.value = 0

    def is_leaf(self):
        return self.value is not None and not (self.left and self.right)

    def magnitude(self):
        if self.is_leaf():
            return self.value
        return 3*self.left.magnitude() + 2*self.right.magnitude()

    def split(self):
        self.left = Node(self, math.floor(self.value / 2))
        self.right = Node(self, math.ceil(self.value / 2))
        self.value = None

    def __str__(self):
        if self.is_leaf():
            return str(self.value)
        else:
            return f'[{str(self.left)},{str(self.right)}]'

class SnailfishNumber:
    @classmethod
    def parse(cls, number):
        return cls(Node.parse(number))

    def __init__(self, root):
        self.root = root

    def add(self, sfn):
        new_root = Node(None)
        new_root.left = self.root
        new_root.right = sfn.root
        self.root.parent = new_root
        sfn.root.parent = new_root
        self.root = new_root
        self.reduce()

    def reduce(self):
        action = True
        while action:
            action = False
            if self._explode():
                action = True
            elif self._split():
                action = True

    def _explode(self):
        nodes = [self.root]
        while nodes != []:
            node = nodes.pop()
            if node.depth() == 4 and not node.is_leaf():
                node.explode()
                return True
            if not node.is_leaf():
                nodes.append(node.right)
                nodes.append(node.left)
        return False

    def _split(self):
        nodes = [self.root]
        while nodes != []:
            node = nodes.pop()
            if node.is_leaf() and node.value >= 10:
                node.split()
                return True
            if not node.is_leaf():
                nodes.append(node.right)
                nodes.append(node.left)
        return False

def part_1(numbers):
    total = numbers.pop(0)
    for number in numbers:
        total.add(number)
    return total.root.magnitude()

def part_2(numbers):
    max_magnitude = 0
    for i in numbers:
        for j in numbers:
            i_copy = SnailfishNumber(i.root.copy())
            j_copy = SnailfishNumber(j.root.copy())
            i_copy.add(j_copy)
            max_magnitude = max(max_magnitude, i_copy.root.magnitude())
    return max_magnitude

def read_numbers(path):
    numbers = []
    with open(path, 'r') as f:
        for number in f.readlines():
            numbers.append(SnailfishNumber.parse(number.rstrip()))
    return numbers


if __name__ == '__main__':
    print(part_1(read_numbers('input')))
    print(part_2(read_numbers('input')))
