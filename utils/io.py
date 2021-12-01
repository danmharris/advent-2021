def read_ints(path):
    with open(path, 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]
