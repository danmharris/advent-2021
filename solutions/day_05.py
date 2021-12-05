import re

def part_1(lines):
    lines = [line for line in lines if _is_straight(line)]
    return _find_danger(lines)

def part_2(lines):
    lines = [line for line in lines if _is_straight(line) or _is_diag(line)]
    return _find_danger(lines)

def read_lines(path):
    with open(path, 'r') as f:
        lines = []
        pat = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
        for l in f:
            groups = [int(val) for val in pat.match(l).groups()]
            lines.append([(groups[0], groups[1]), (groups[2], groups[3])])
        return lines


def _find_danger(lines):
    danger_points = {}
    for line in lines:
        point = line[0]
        fin = line[1]

        x_step = _get_step(point[0], fin[0])
        y_step = _get_step(point[1], fin[1])

        while True:
            if point not in danger_points:
                danger_points[point] = 0
            danger_points[point] = danger_points[point] + 1
            if point == fin:
                break
            point = (point[0] + x_step, point[1] + y_step)
    danger_points = [point for (point, count) in danger_points.items() if count >= 2]
    return len(danger_points)


def _get_step(p1, p2):
    if p2 > p1:
        return 1
    if p2 == p1:
        return 0
    return -1


def _is_straight(line):
    p1 = line[0]
    p2 = line[1]
    return p1[0] == p2[0] or p1[1] == p2[1]


def _is_diag(line):
    p1 = line[0]
    p2 = line[1]
    return abs(p2[0] - p1[0]) == abs(p2[1] - p1[1])


if __name__ == '__main__':
    print(part_1(read_lines('input')))
    print(part_2(read_lines('input')))
