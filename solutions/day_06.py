from utils.io import read_csv

def part_1(timers):
    return _reproduce(timers[:], 80)

def part_2(timers):
    return _reproduce_counts(timers[:], 256)


# Initial idea for part 1 but far too slow for part 2
def _reproduce(timers, days):
    for _ in range(0, days):
        for (index, timer) in enumerate(timers[:]):
            new_timer = timer - 1
            if new_timer < 0:
                new_timer = 6
                timers.append(8)
            timers[index] = new_timer
    return len(timers)


# Revised idea for part 2 using frequencies rather than tracking each fish
def _reproduce_counts(timers, days):
    counts = []
    counts = [0 for i in range(0, 9)]
    for timer in timers:
        counts[timer] = counts[timer] + 1

    for _ in range(0, days):
        new_counts = [0 for i in range(0, 9)]
        for timer, count in enumerate(counts):
            if timer == 0:
                new_counts[8] = count
                new_counts[6] = count
                continue
            new_counts[timer-1] = new_counts[timer-1] + count
        counts = new_counts
    return sum(counts)


if __name__ == '__main__':
    print(part_1(read_csv('input')))
    print(part_2(read_csv('input')))
