import copy

def build_empty_grid(size):
    """

    :param size:
    :return:
    """
    grid = []
    for row in range(size):
        newRow = []
        for col in range(size):
            newRow.append(False)
        grid.append(newRow)
    return grid

def getPoint(point):
    return point[0],point[1]

def build_grid(size,startPositions):
    """

    :param startPositions: list of points of live cells
    :return: new grid
    """
    grid = build_empty_grid(size)
    for point in startPositions:
        x,y = getPoint(point)
        grid[y][x] = True
    return grid

def check_neighbors(grid,point):
    """

    :param grid: 2D grid
    :param point: (x,y)
    :return:
    """
    neighbors =0
    x, y = getPoint(point)
    for row in range(-1,2):
        for col in range(-1,2):
            if row ==0 and col ==0 : continue
            if grid[y+row][x+col]:
                neighbors+=1
    return neighbors


def turn(grid):
    size = len(grid)
    newGrid = build_empty_grid(size)
    for row in range(size):
        for col in range(size):
            neighbors = check_neighbors(grid,(col,row))


def play():
    pass