def part_1(patterns):
    outputs = [output for pat in patterns for output in pat[1]]
    uniques = [2, 3, 4, 7]
    count = 0
    for output in outputs:
        if len(output) in uniques:
            count = count + 1
    return count

def part_2(patterns):
    total = 0
    for inputs, outputs in patterns:
        inputs = [set(i) for i in inputs]
        mapping = {}
        mapping[1] = [i for i in inputs if len(i) == 2][0]
        mapping[7] = [i for i in inputs if len(i) == 3][0]
        mapping[4] = [i for i in inputs if len(i) == 4][0]
        mapping[8] = [i for i in inputs if len(i) == 7][0]

        fives = [i for i in inputs if len(i) == 5]
        sixes = [i for i in inputs if len(i) == 6]

        for s in sixes[:]:
            if not mapping[1].issubset(s):
                mapping[6] = s
                sixes.remove(s)
            if mapping[4].issubset(s):
                mapping[9] = s
                sixes.remove(s)
        mapping[0] = sixes.pop()

        for f in fives[:]:
            if mapping[1].issubset(f):
                mapping[3] = f
                fives.remove(f)
            if f.issubset(mapping[6]):
                mapping[5] = f
                fives.remove(f)
        mapping[2] = fives.pop()

        rev_mapping = {frozenset(v): str(k) for k, v in mapping.items()}
        outputs = [frozenset(o) for o in outputs]
        number = ''
        for output in outputs:
            number = number + rev_mapping[output]
        total = total + int(number)
    return total

def read_patterns(path):
    with open(path, 'r') as f:
        patterns = []
        for line in f:
            parts = line.split('|')
            inputs = parts[0].strip().split()
            outputs = parts[1].strip().split()
            patterns.append((inputs, outputs))
        return patterns


if __name__ == '__main__':
    print(part_1(read_patterns('input')))
    print(part_2(read_patterns('input')))
