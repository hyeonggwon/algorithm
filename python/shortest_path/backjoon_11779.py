import sys
import heapq

def dijkstra(start):
    q = []
    d[start] = 0
    p[start] = [start]
    heapq.heappush(q, (0, start, [start]))
    while q:
        cost, node, path = heapq.heappop(q)
        if d[node] < cost:
            continue
        for next, c in graph[node]:
            next_cost = cost + c
            if next_cost < d[next]:
                d[next] = next_cost
                p[next] = path + [next]
                heapq.heappush(q, (next_cost, next, p[next]))

INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
d = [INF] * (N + 1)
p = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

dijkstra(start)

print(d[end])
print(len(p[end]))
print(*p[end])