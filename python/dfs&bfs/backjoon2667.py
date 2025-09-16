dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt):
    cnt += 1
    graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != 1:
            continue
        cnt = dfs(nx, ny, cnt)
    return cnt

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_cnt = dfs(i, j, 0)
            answer.append(house_cnt)
answer.sort()
print(len(answer))
for house_cnt in answer:
    print(house_cnt)