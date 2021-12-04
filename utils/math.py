def transpose(grid):
    transposed = []
    for i in range(0, len(grid[0])):
        transposed.append([])
    for row in grid:
        for (i, val) in enumerate(row):
            transposed[i].append(val)
    return transposed
