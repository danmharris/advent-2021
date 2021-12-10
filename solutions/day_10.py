from math import floor

from utils.io import read_strings

OPENING = ['(', '[', '{', '<']
CLOSING = [')', ']', '}', '>']

def part_1(data):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total = 0
    for line in data:
        stack = []
        for char in line:
            if char in OPENING:
                stack.append(char)
                continue
            curr = CLOSING.index(char)
            match = OPENING.index(stack.pop())
            if curr != match:
                total += points[char]
                break
    return total

def part_2(data):
    scores = []
    for line in data:
        stack = []
        corrupted = False
        for char in line:
            if char in OPENING:
                stack.append(char)
                continue
            curr = CLOSING.index(char)
            match = OPENING.index(stack.pop())
            if curr != match:
                corrupted = True
                break
        if corrupted:
            continue
        score = 0
        for _ in range(0, len(stack)):
            index = OPENING.index(stack.pop())
            score = score * 5 + index + 1
        scores.append(score)
    return sorted(scores)[floor(len(scores)/2)]


if __name__ == '__main__':
    print(part_1(read_strings('input')))
    print(part_2(read_strings('input')))
