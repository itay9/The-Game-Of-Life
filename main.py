import copy
from time import sleep

#Author: Itay Dali


SIGN='@'

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

def check_range(grid,point):
    size = len(grid)
    x,y=getPoint(point)
    return x>=0 and x<size and y>=0 and y<size
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
            if not check_range(grid,(col+x,row+y)) : continue
            if grid[y+row][x+col]:
                neighbors+=1
    return neighbors


def play_turn(grid):
    size = len(grid)
    newGrid =copy.deepcopy(grid)
    for row in range(size):
        for col in range(size):
            neighbors = check_neighbors(grid,(col,row))
            if grid[row][col] and (neighbors!=2 or neighbors!=3):
                newGrid[row][col] = False
            if (not grid[row][col]) and  neighbors==3:
                newGrid[row][col] = True
    return newGrid

def print_grid(grid,turn):
    print("*******************")
    print()
    print("turn number:",turn)
    print()
    size = len(grid)
    print('_'*(size+2))
    for row in range(size):
        print('|',end='')
        for col in range(size):
            if grid[row][col]: print(SIGN,end='')
            else : print(' ',end='')
        print('|')
    print('_' * (size + 2))
    print()
    print("*******************")

def check_still_alive(grid):
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if grid[row][col]: return True
    return False

def play_game(turns):
    startPositions = [(9,9),(10,9),(10,10),(8,8),(7,8),(30,31),(30,32),(30,33),(32,31),(30,35),(32,33),(34,31),(34,32),(34,33)]
    size = 50
    DELAY = 1
    grid = build_grid(size,startPositions)
    print_grid(grid,0)
    for turn in range(1,turns+1):
        grid = play_turn(grid)
        if check_still_alive(grid):
            print_grid(grid,turn)
            sleep(DELAY)
        else:
            print("all dead! in",turn,"turns")
            print_grid(grid,turn)
            break


play_game(15)
