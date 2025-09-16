dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, graph, n):
    graph[x][y] = 2
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            count += dfs(nx, ny, graph, n)
    return count

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