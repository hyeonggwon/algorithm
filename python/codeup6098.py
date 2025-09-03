def nextDir(x, y):
    global array
    if array[x][y + 1] == 0 or array[x][y + 1] == 2:
        return 0
    elif array[x + 1][y] == 0 or array[x + 1][y] == 2:
        return 1
    else:
        return 2

array = []
for i in range(10):
    array.append(list(map(int, input().split())))

x, y = 1, 1
dir = 0
while True:
    if array[x][y] == 2:
        array[x][y] = 9
        break
    array[x][y] = 9
    next = nextDir(x, y)
    if next == 0:
        y += 1
    elif next == 1:
        x += 1
    else:
        break

for i in range(10):
    print(' '.join(map(str, array[i])))