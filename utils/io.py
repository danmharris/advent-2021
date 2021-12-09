def read_ints(path):
    with open(path, 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]

def read_actions(path):
    with open(path, 'r') as f:
        actions = []
        for line in f:
            tokens = line.rstrip().split()
            actions.append((tokens[0], int(tokens[1])))
        return actions

def read_strings(path):
    with open(path, 'r') as f:
        return [line.rstrip() for line in f.readlines()]

def read_csv(path):
    with open(path, 'r') as f:
        return [int(val) for val in f.readline().rstrip().split(',')]

def read_grid(path):
    with open(path, 'r') as f:
        return [[int(val) for val in row.rstrip()] for row in f.readlines()]
