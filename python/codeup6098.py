PATH = 0
WALL = 1
FOOD = 2
VISITED = 9

RIGHT = 0
DOWN = 1
NONE = 2

def nextDir(x, y, maze):
    if maze[x][y + 1] == PATH or maze[x][y + 1] == FOOD:
        return RIGHT
    elif maze[x + 1][y] == PATH or maze[x + 1][y] == FOOD:
        return DOWN
    else:
        return NONE

array = []
for i in range(10):
    array.append(list(map(int, input().split())))

x, y = 1, 1
while True:
    if array[x][y] == FOOD:
        array[x][y] = VISITED
        break
    array[x][y] = VISITED
    next_move = nextDir(x, y, array)
    if next_move == RIGHT:
        y += 1
    elif next_move == DOWN:
        x += 1
    else:
        break

for i in range(10):
    print(' '.join(map(str, array[i])))