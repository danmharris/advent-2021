def part_1(algo, image):
    return enhance_n(algo, image, 2)

def part_2(algo, image):
    return enhance_n(algo, image, 50)

def enhance(algo, image):
    points = list(image.keys())
    points.sort(key=lambda point: point[1])
    min_y, max_y = points[0][1], points[len(points)-1][1]
    points.sort(key=lambda point: point[0])
    min_x, max_x = points[0][0], points[len(points)-1][0]

    new_image = {}
    for y in range(min_y-1, max_y+2):
        for x in range(min_x-1, max_x+2):
            string = '0b'
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    val = image.get((i, j), image[(min_x, min_y)])
                    string += '1' if val else '0'
            new_image[(x, y)] = algo[int(string, base=2)]
    return new_image

def enhance_n(algo, image, n):
    image = surround(image)
    for _ in range(0, n):
        image = enhance(algo, image)
    return len([point for point, val in image.items() if val is True])

def read_image(path):
    with open(path, 'r') as f:
        enhance_line = f.readline().rstrip()
        algo = [char == '#' for char in enhance_line]
        f.readline()

        image = {}
        for y, l in enumerate(f.readlines()):
            for x, char in enumerate(l.rstrip()):
                image[(x, y)] = char == '#'
        return algo, image

def surround(image):
    points = list(image.keys())
    points.sort(key=lambda point: point[1])
    min_y, max_y = points[0][1], points[len(points)-1][1]
    points.sort(key=lambda point: point[0])
    min_x, max_x = points[0][0], points[len(points)-1][0]

    new_image = {}
    for y in range(min_y-1, max_y+2):
        for x in range(min_x-1, max_x+2):
            if (x, y) in image:
                new_image[(x, y)] = image[(x, y)]
            else:
                new_image[(x, y)] = False
    return new_image


if __name__ == '__main__':
    algo, image = read_image('input')
    print(part_1(algo, image.copy()))
    print(part_2(algo, image.copy()))
