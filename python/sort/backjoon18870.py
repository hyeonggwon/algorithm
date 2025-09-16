import bisect

n = int(input())
X = list(map(int, input().split()))
mapper = [0] * n

for i in range(n):
    mapper[i] = X[i]

X = list(set(X))
X.sort()

coord_map = {val: i for i, val in enumerate(X)}
result = [coord_map[val] for val in mapper]

print(*result)