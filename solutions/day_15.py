import math

from utils.io import read_grid
from utils.math import grid_generator

class Dijkstra:
    def __init__(self, grid, repeats=1):
        self.distance = {}
        self.prev = {}
        self.unvisited = {(0, 0)}
        self.visited = set()
        self.distance[(0, 0)] = 0
        self.grid = grid
        self.repeats = repeats

    def solve(self):
        max_x = self.repeats * len(self.grid[0]) - 1
        max_y = self.repeats * len(self.grid) - 1

        curr_node = (0, 0)
        while True:
            x, y = curr_node
            if x > 0:
                self._check_neighbour(curr_node, (x-1, y))
            if x < max_x:
                self._check_neighbour(curr_node, (x+1, y))
            if y > 0:
                self._check_neighbour(curr_node, (x, y-1))
            if y < max_y:
                self._check_neighbour(curr_node, (x, y+1))
            if self.distance.get((max_x, max_y), math.inf) < math.inf:
                break
            self.unvisited.remove(curr_node)
            self.visited.add(curr_node)
            curr_node = min(self.unvisited, key=lambda n: self.distance[n])
        curr_node = (max_x, max_y)
        cost = 0
        while curr_node != (0, 0):
            cost += self._get_risk(curr_node)
            curr_node = self.prev[curr_node]
        return cost

    def _check_neighbour(self, point, neighbour):
        new_distance = self.distance[point] + self._get_risk(neighbour)
        if new_distance < self.distance.get(neighbour, math.inf):
            self.distance[neighbour] = new_distance
            self.prev[neighbour] = point
        if neighbour not in self.visited:
            self.unvisited.add(neighbour)

    def _get_risk(self, point):
        x, y = point

        val = self.grid[y % len(self.grid)][x % len(self.grid[0])]
        repeats_x = math.floor(x / len(self.grid[0]))
        repeats_y = math.floor(y / len(self.grid))
        repeats = repeats_x + repeats_y

        new_val = val + repeats
        if new_val > 9:
            new_val -= 9
        return new_val


def part_1(grid):
    return Dijkstra(grid).solve()

def part_2(grid):
    return Dijkstra(grid, 5).solve()


if __name__ == '__main__':
    print(part_1(read_grid('input')))
    print(part_2(read_grid('input')))
