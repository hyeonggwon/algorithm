import heapq

# 매 순간마다 가장 작은 수를 더해서 넣는 게 최적의 수임
# 모든 숫자를 우선순위 큐에 넣고, 가장 작은 수 두개를 빼서 더하고 넣기를 반복해서 풀이
# 시간복잡도 : O(m log n)
N, M = map(int, input().split())
numq = list(map(int, input().split()))

heapq.heapify(numq)

for _ in range(M):
    a, b = heapq.heappop(numq), heapq.heappop(numq)
    heapq.heappush(numq, a + b)
    heapq.heappush(numq, a + b)

print(sum(numq))