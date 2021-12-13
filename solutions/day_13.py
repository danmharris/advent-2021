import re

def part_1(grid, folds):
    for direction, pos in folds[:1]:
        _fold(direction, pos, grid)
    return len(grid.keys())

def part_2(grid, folds):
    for direction, pos in folds:
        _fold(direction, pos, grid)
    max_x = max([pos[0] for pos in grid.keys()])
    max_y = max([pos[1] for pos in grid.keys()])
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            print('#', end='') if (x, y) in grid else print(' ', end='')
        print()

def read_paper(path):
    with open(path, 'r') as f:
        read_points = False
        grid = {}
        folds = []
        fold_regex = re.compile(r'fold along (\w)=(\d+)')
        for line in f.readlines():
            line = line.rstrip()
            if line == '':
                read_points = True
                continue
            if read_points:
                groups = fold_regex.match(line).groups()
                folds.append((groups[0], int(groups[1])))
            else:
                point = line.split(',')
                grid[(int(point[0]), int(point[1]))] = True
        return grid, folds


def _fold(direction, pos, grid):
    if direction == 'x':
        # Because its 0-indexed and this is the middle we know theres pos
        # values either side of the fold
        for i in range(1, pos+1):
            points = [point for point in grid.keys() if point[0] == pos+i]
            for x, y in points:
                grid[(pos-i, y)] = True
                del grid[(x, y)]
    if direction == 'y':
        for i in range(1, pos+1):
            points = [point for point in grid.keys() if point[1] == pos+i]
            for x, y in points:
                grid[(x, pos-i)] = True
                del grid[(x, y)]


if __name__ == '__main__':
    grid, folds = read_paper('input')
    print(part_1(grid, folds))
    part_2(grid, folds[1:])  # Already done first fold for part 1
