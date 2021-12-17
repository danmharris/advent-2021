def fire(vel_x, vel_y, target_x, target_y):
    min_x, max_x = target_x
    min_y, max_y = target_y

    gen_x = _move_x(vel_x)
    gen_y = _move_y(vel_y)

    curr_x, curr_y = 0, 0
    while True:
        curr_x = next(gen_x)
        curr_y = next(gen_y)
        if curr_x >= min_x and curr_x <= max_x and curr_y >= min_y and curr_y <= max_y:
            return True
        if curr_x > max_x or curr_y < min_y:
            return False

def part_1(target_x, target_y):
    min_x, max_x = target_x
    min_y, max_y = target_y

    best_max_height = 0
    for vel_y in range(min_y, abs(min_y)+1):
        for vel_x in range(0, max_x+1):
            if fire(vel_x, vel_y, target_x, target_y):
                best_max_height = int(vel_y * (vel_y + 1) / 2)
    return best_max_height

def part_2(target_x, target_y):
    min_x, max_x = target_x
    min_y, max_y = target_y

    vel_count = 0
    for vel_y in range(min_y, abs(min_y)+1):
        for vel_x in range(0, max_x+1):
            if fire(vel_x, vel_y, target_x, target_y):
                vel_count += 1
    return vel_count


def _move_x(vel_x):
    curr_x = 0
    while True:
        curr_x += vel_x
        if vel_x > 0:
            vel_x -= 1
        elif vel_x < 0:
            vel_x += 1
        yield curr_x


def _move_y(vel_y):
    curr_y = 0
    while True:
        curr_y += vel_y
        vel_y -= 1
        yield curr_y


if __name__ == '__main__':
    print(part_1((29, 73), (-248, -194)))
    print(part_2((29, 73), (-248, -194)))
