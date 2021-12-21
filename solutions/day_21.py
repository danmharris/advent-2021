import functools

def part_1(pos):
    current_player = 0
    pos = [p-1 for p in pos]
    score = [0 for _ in pos]
    for turn in range(3, 3000, 3):
        sum_to_turn = int(turn*(turn+1)/2)
        sum_to_prev = int((turn-3)*(turn-2)/2)
        to_move = sum_to_turn - sum_to_prev
        pos[current_player] = (pos[current_player] + to_move) % 10
        score[current_player] += pos[current_player] + 1

        next_player = (current_player + 1) % len(pos)
        if score[current_player] >= 1000:
            return score[next_player] * turn
        current_player = next_player

def part_2(pos):
    pos = [p-1 for p in pos]
    score = [0 for _ in pos]
    wins = play(tuple(pos), tuple(score))
    return max(wins)


@functools.lru_cache(maxsize=None)
def play(pos, score, turn=-1, roll=None):
    """
    Keep track of which roll it is (starting from 0), when % 3 is 2 its the
    third roll so add the score then. % 6 lets us work out the player, as 0-2
    will be player 1, and 3-5 will be player 2.

    pos and score need to be tuples because they need to be hashable for
    lru_cache to work.
    """
    player = 0 if (turn % 6) < 3 else 1
    if roll is not None:
        if player == 0:
            pos = ((pos[0] + roll) % 10, pos[1])
            if turn % 3 == 2:
                score = ((score[0] + pos[0] + 1), score[1])
        elif player == 1:
            pos = (pos[0], (pos[1] + roll) % 10)
            if turn % 3 == 2:
                score = (score[0], (score[1] + pos[1] + 1))

        if score[player] >= 21:
            if player == 0:
                return [1, 0]
            else:
                return [0, 1]

    wins = [0, 0]
    for i in range(1, 4):
        res = play(pos, score, turn+1, i)
        wins[0] += res[0]
        wins[1] += res[1]
    return wins


if __name__ == '__main__':
    print(part_1([6, 1]))
    print(part_2([6, 1]))
