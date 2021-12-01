from solutions.util.io import read_ints

def part_1(lines):
    increases = -1
    prev = 0

    for line in lines:
        if line > prev:
            increases = increases + 1
        prev = line
    return increases

def part_2(lines):
    increases = -1
    prev = 0
    for window in (lines[i:i+3] for i in range(len(lines) - 3 + 1)):
        val = sum(window)
        if val > prev:
            increases = increases + 1
        prev = val
    return increases


if __name__ == '__main__':
    print(part_1(read_ints('input')))
    print(part_2(read_ints('input')))
