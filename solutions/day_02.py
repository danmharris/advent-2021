from utils.io import read_actions

def part_1(actions):
    horizontal = 0
    depth = 0
    for (action, val) in actions:
        if action == 'forward':
            horizontal = horizontal + val
        elif action == 'down':
            depth = depth + val
        elif action == 'up':
            depth = depth - val
    return horizontal * depth

def part_2(actions):
    horizontal = 0
    depth = 0
    aim = 0
    for (action, val) in actions:
        if action == 'down':
            aim = aim + val
        elif action == 'up':
            aim = aim - val
        elif action == 'forward':
            horizontal = horizontal + val
            depth = depth + (aim * val)
    return horizontal * depth


if __name__ == '__main__':
    print(part_1(read_actions('input')))
    print(part_2(read_actions('input')))
