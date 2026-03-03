# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# dirs = ['L', 'R', 'U', 'D']
#
# for plan in plans:
#     for i in range(len(dirs)):
#         if plan == dirs[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or nx > n or ny < 1 or ny > n:
#         continue
#     x = nx
#     y = ny
# print(x, y)































dir_map = {'R':0, 'L':1, 'D':2, 'U':3}
dx = [0, 0, 1, -1]
dy = [1, -1, 0 , 0]

n = int(input())
plan = input().split()
x, y = 1, 1

for dir in plan:
    if dir not in ['R', 'L', 'D', 'U']:
        continue
    nx = x + dx[dir_map.get(dir)]
    ny = y + dy[dir_map.get(dir)]

    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(x, y)