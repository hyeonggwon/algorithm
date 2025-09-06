GROUND = 0
SEA = 1
VISITED = 2

n, m = map(int, input().split())
x, y, curDir = map(int, input().split())
totalMap = [list(map(int, input().split())) for _ in range(n)]

def rotate(curDir):
    return (curDir - 1) % 4

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

totalMap[y][x] = VISITED
while True:
    isMoved = False
    for i in range(4):
        curDir = rotate(curDir)
        nx = x + dx[curDir]
        ny = y + dy[curDir]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if totalMap[ny][nx] == GROUND:
            totalMap[ny][nx] = VISITED
            x = nx
            y = ny
            isMoved = True
            break
    if isMoved:
        continue
    nx = x - dx[curDir]
    ny = y - dy[curDir]
    if nx < 0 or ny < 0 or nx >= m or ny >= n or totalMap[ny][nx] == SEA:
        break
    x = nx
    y = ny
    print(x, y)
count = 0
for i in range(n):
    count += totalMap[i].count(VISITED)
print(totalMap)
print(count)