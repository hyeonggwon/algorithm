# pos = input()
# x, y = ord(pos[0]) - ord('a') + 1, int(pos[1])
#
# dx = [-1, 1, -2, 2, -2, 2, -1, 1]
# dy = [-2, -2, -1, -1, 1, 1, 2, 2]
#
# result = 0
# for i in range(8):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > 8 or  ny > 8:
#         continue
#     result += 1
# print(result)



















x, y = list(input())
x = ord(x) - ord('a') + 1
y = int(y)

dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]

result = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        result += 1

print(result)