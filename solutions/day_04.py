import functools

from utils.math import transpose

class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.transposed = transpose(board)
        self.won = False
    def mark_number(self, num):
        self.current_num = num
        for row in self.board + self.transposed:
            if num in row:
                row.remove(num)
            if len(row) == 0:
                self.won = True
        return self
    def has_won(self):
        return self.won
    def score(self):
        if not self.has_won():
            raise Exception("hasn't won!")
        unmarked = functools.reduce(lambda x, y: x+y, self.board)
        return sum(unmarked) * self.current_num

def part_1(numbers, boards):
    for num in numbers:
        for board in boards:
            if board.mark_number(num).has_won():
                return board.score()

def part_2(numbers, boards):
    most_recent_winner = None
    for num in numbers:
        for board in boards[:]:
            if board.mark_number(num).has_won():
                most_recent_winner = board
                boards.remove(board)
        if len(boards) == 0:
            break
    return most_recent_winner.score()

def read_bingo(path):
    with open(path, 'r') as f:
        numbers = [int(n) for n in f.readline().rstrip().split(',')]
        f.readline()

        grids = []
        current_grid = []
        for line in f:
            if line == "\n":
                grids.append(BingoBoard(current_grid))
                current_grid = []
                continue
            current_grid.append([int(n) for n in line.rstrip().split()])
        grids.append(BingoBoard(current_grid))
        return numbers, grids


if __name__ == '__main__':
    numbers, boards = read_bingo('input')
    print(part_1(numbers, boards))
    print(part_2(numbers, boards))
