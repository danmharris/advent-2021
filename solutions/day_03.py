from utils.io import read_strings

def part_1(lines):
    gamma_string = "0b"
    epsilon_string = "0b"
    for i in range(0, len(lines[0])):
        elements = [line[i] for line in lines]
        if _count_freq(elements) > 0:
            gamma_string = gamma_string + "1"
            epsilon_string = epsilon_string + "0"
        else:
            gamma_string = gamma_string + "0"
            epsilon_string = epsilon_string + "1"
    return int(gamma_string, base=2) * int(epsilon_string, base=2)

def part_2(lines):
    return _match_criteria(lines, False) * _match_criteria(lines, True)


def _match_criteria(lines, least_common=False):
    remaining = lines
    for i in range(0, len(lines[0])):
        count = _count_freq([line[i] for line in remaining])
        most_freq = ""
        if least_common:
            most_freq = "0" if count >= 0 else "1"
        else:
            most_freq = "1" if count >= 0 else "0"
        if len(remaining) > 1:
            remaining = [line for line in remaining if line[i] == most_freq]
    return int(remaining[0], base=2)

def _count_freq(a):
    total = 0
    for i in a:
        if i == '1':
            total = total + 1
        else:
            total = total - 1
    return total


if __name__ == '__main__':
    print(part_1(read_strings('input')))
    print(part_2(read_strings('input')))
