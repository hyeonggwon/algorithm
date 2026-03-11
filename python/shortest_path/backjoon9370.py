import sys
import heapq

def dijkstra(d, start):
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if d[node] < dist:
            continue
        for next, cost in graph[node]:
            next_dist = dist + cost
            if next_dist < d[next]:
                d[next] = next_dist
                heapq.heappush(q, (next_dist, next))

INF = sys.maxsize
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    sd = [INF] * (n + 1)
    gd = [INF] * (n + 1)
    hd = [INF] * (n + 1)
    gh_len = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if a == g and b == h or a == h and b == g:
            gh_len = d
    targets = [int(input()) for _ in range(t)]

    dijkstra(sd, s)
    dijkstra(gd, g)
    dijkstra(hd, h)

    targets.sort()

    for x in targets:
        dist = min(sd[g] + gh_len + hd[x], sd[h] + gh_len + gd[x])
        if dist < INF and dist == sd[x]:
            print(x, end=' ')