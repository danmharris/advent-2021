import re

def part_1(template, rules):
    counts = {}
    for el in template:
        if el not in counts:
            counts[el] = 0
        counts[el] += 1

    for _ in range(0, 10):
        new_template = template[0]
        for p in zip(template[:], template[1:]):
            pair = ''.join(p)
            new_el = rules[pair]
            new_template += new_el + pair[1]
            if new_el not in counts:
                counts[new_el] = 0
            counts[new_el] += 1
        template = new_template

    count_vals = counts.values()
    return max(count_vals) - min(count_vals)

def part_2(template, rules):
    counts = {}
    for el in template:
        if el not in counts:
            counts[el] = 0
        counts[el] += 1

    rule_counts = {rule: 0 for rule in rules.keys()}
    for p in zip(template[:], template[1:]):
        pair = ''.join(p)
        rule_counts[pair] += 1

    for _ in range(0, 40):
        new_rule_counts = dict(rule_counts)
        for pair, count in rule_counts.items():
            new_el = rules[pair]

            new_1 = pair[0] + new_el
            new_2 = new_el + pair[1]

            new_rule_counts[new_1] += count
            new_rule_counts[new_2] += count
            new_rule_counts[pair] -= count

            if new_el not in counts:
                counts[new_el] = 0
            counts[new_el] += count
        rule_counts = new_rule_counts

    count_vals = counts.values()
    return max(count_vals) - min(count_vals)

def read_polymer_template(path):
    with open(path, 'r') as f:
        template = f.readline().rstrip()
        f.readline()

        rule = re.compile(r'(\w{2}) -> (\w{1})')
        rules = {}
        for line in f.readlines():
            groups = rule.match(line.rstrip()).groups()
            rules[groups[0]] = groups[1]
        return template, rules


if __name__ == '__main__':
    template, rules = read_polymer_template('input')
    print(part_1(template, rules))
    print(part_2(template, rules))
