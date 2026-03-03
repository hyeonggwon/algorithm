# GROUND = 0
# SEA = 1
# VISITED = 2
#
# n, m = map(int, input().split())
# x, y, curDir = map(int, input().split())
# totalMap = [list(map(int, input().split())) for _ in range(n)]
#
# def rotate(curDir):
#     return (curDir - 1) % 4
#
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
#
# totalMap[y][x] = VISITED
# count = 1
# while True:
#     isMoved = False
#     for i in range(4):
#         curDir = rotate(curDir)
#         nx = x + dx[curDir]
#         ny = y + dy[curDir]
#         if nx < 0 or ny < 0 or nx >= m or ny >= n:
#             continue
#         if totalMap[ny][nx] == GROUND:
#             totalMap[ny][nx] = VISITED
#             x = nx
#             y = ny
#             isMoved = True
#             count += 1
#             break
#     if isMoved:
#         continue
#     nx = x - dx[curDir]
#     ny = y - dy[curDir]
#     if nx < 0 or ny < 0 or nx >= m or ny >= n or totalMap[ny][nx] == SEA:
#         break
#     x = nx
#     y = ny
# print(count)



















dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(n)]

while True:
    moved = False
    for _ in range(4):
        d = (d - 1) % 4

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and total_map[nx][ny] == 0:
            total_map[nx][ny] = 2
            x, y = nx, ny
            moved = True
            break

    if not moved:
        nx = x + dx[(d + 2) % 4]
        ny = y + dy[(d + 2) % 4]

        if 0 <= nx < n and 0 <= ny < n and total_map[nx][ny] == 2:
            x, y = nx, ny
            continue
        else:
            break

print(sum(x.count(2) for x in total_map))