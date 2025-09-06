pos = input()
x, y = ord(pos[0]) - ord('a') + 1, int(pos[1])

dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]

result = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or  ny > 8:
        continue
    print(nx, ny)
    result += 1
print(result)