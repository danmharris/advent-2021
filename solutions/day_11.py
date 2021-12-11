from utils.io import read_grid

def part_1(grid):
    flashes = 0
    for _ in range(0, 100):
        flashes += _step(grid)
    return flashes

def part_2(grid):
    step = 0
    while True:
        step += 1
        if _step(grid) == 100:
            return step


def _step(grid):
    flashes = 0
    flashed = []

    # Step 1: Increase all by 1. Keep track of those going to flash
    for x, y in _grid_generator(10, 10):
        if grid[y][x] == 9:
            flashed.append((x, y))
            flashes += 1
        grid[y][x] += 1

    # Step 2: Increase neighbours of each flash until no new flashes occur
    while len(flashed) > 0:
        x, y = flashed.pop(0)
        for cy in range(max(0, y-1), min(10, y+2)):
            for cx in range(max(0, x-1), min(10, x+2)):
                if grid[cy][cx] == 9:
                    flashed.append((cx, cy))
                    flashes += 1
                grid[cy][cx] += 1

    # Step 3: Zero out all flashed values
    for x, y in _grid_generator(10, 10):
        if grid[y][x] > 9:
            grid[y][x] = 0
    return flashes


def _grid_generator(len_x, len_y):
    for y in range(0, len_y):
        for x in range(0, len_x):
            yield x, y


if __name__ == '__main__':
    print(part_1(read_grid('input')))
    print(part_2(read_grid('input')))
