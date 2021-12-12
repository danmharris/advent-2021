class CaveSystem:
    def __init__(self, paths, allow_revisit=False):
        self.neighbours = _get_neighbours(paths)
        self.paths = []
        self.allow_revisit = allow_revisit
    def add_path(self, path):
        self.paths.append(path)
    def count_paths(self):
        return len(self.paths)
    def find_paths(self):
        return self._find_paths('start', [])

    def _find_paths(self, point, curr_path, has_revisited=False):
        if point == 'start' and len(curr_path) > 0:
            return self
        if point.lower() == point and point in curr_path:
            if has_revisited or not self.allow_revisit:
                return self
            has_revisited = True

        curr_path.append(point)

        if point == 'end':
            self.add_path(curr_path)
            return self

        for neighbour in self.neighbours[point]:
            self._find_paths(neighbour, curr_path[:], has_revisited)
        return self

def part_1(paths):
    return CaveSystem(paths, False).find_paths().count_paths()

def part_2(paths):
    return CaveSystem(paths, True).find_paths().count_paths()

def read_paths(path):
    with open(path, 'r') as f:
        return [tuple(line.rstrip().split('-')) for line in f.readlines()]


def _get_neighbours(paths):
    neighbours = {}
    for p1, p2 in paths:
        if p1 not in neighbours:
            neighbours[p1] = set()
        neighbours[p1].add(p2)
        if p2 not in neighbours:
            neighbours[p2] = set()
        neighbours[p2].add(p1)
    return neighbours


if __name__ == '__main__':
    print(part_1(read_paths('input')))
    print(part_2(read_paths('input')))
