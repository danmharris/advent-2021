import statistics

from utils.io import read_csv

def part_1(positions):
    median = round(statistics.median(positions))
    costs = [abs(pos-median) for pos in positions]
    return sum(costs)

def part_2(positions):
    target = round(statistics.median(positions))
    current_cost, prev_cost = None, None

    while True:
        totals = [_find_cost(pos, target) for pos in positions]
        current_cost = sum(totals)
        if prev_cost is not None and current_cost > prev_cost:
            return prev_cost
        prev_cost = current_cost
        target = target + 1


def _find_cost(current, target):
    diff = abs(current-target)
    return int(diff * (diff + 1) / 2)


if __name__ == '__main__':
    print(part_1(read_csv('input')))
    print(part_2(read_csv('input')))
