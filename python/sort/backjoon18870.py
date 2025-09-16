import bisect

n = int(input())
X = list(map(int, input().split()))
mapper = [0] * n

for i in range(n):
    mapper[i] = X[i]

X = list(set(X))
X.sort()

result = [0] * n
for i in range(n):
    result[i] = bisect.bisect_left(X, mapper[i])
print(*result)