import math

from utils.io import read_grid

def part_1(grid):
    total = 0
    for x, y in _find_lows(grid):
        total = total + grid[y][x] + 1
    return total

def part_2(grid):
    basins = []
    for x, y in _find_lows(grid):
        basins.append(_find_basin(grid, [], x, y))
    basins.sort(key=lambda basin: len(basin))
    largest = basins[-3:]
    sizes = [len(basin) for basin in largest]
    return math.prod(sizes)

def _find_basin(grid, basin, x, y):
    if grid[y][x] == 9:
        return basin
    basin.append((x, y))
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    if x > 0 and (x-1, y) not in basin:
        _find_basin(grid, basin, x-1, y)
    if x < max_x and (x+1, y) not in basin:
        _find_basin(grid, basin, x+1, y)
    if y > 0 and (x, y-1) not in basin:
        _find_basin(grid, basin, x, y-1)
    if y < max_y and (x, y+1) not in basin:
        _find_basin(grid, basin, x, y+1)
    return basin


def _find_lows(grid):
    lows = []
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            vals = []
            if x > 0:
                vals.append(row[x-1])
            if x < max_x:
                vals.append(row[x+1])
            if y > 0:
                vals.append(grid[y-1][x])
            if y < max_y:
                vals.append(grid[y+1][x])
            if min(vals) > val:
                lows.append((x, y))
    return lows


if __name__ == '__main__':
    print(part_1(read_grid('input')))
    print(part_2(read_grid('input')))
