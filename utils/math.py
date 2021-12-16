def grid_generator(len_x, len_y):
    for y in range(0, len_y):
        for x in range(0, len_x):
            yield x, y

def transpose(grid):
    transposed = []
    for i in range(0, len(grid[0])):
        transposed.append([])
    for row in grid:
        for (i, val) in enumerate(row):
            transposed[i].append(val)
    return transposed

def hex_to_bin(hex_string):
    bin_string = ''
    for char in hex_string:
        bin_string += format(int(char, base=16), '04b')

    return bin_string
