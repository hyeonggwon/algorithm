n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
result = 0
for i in range(n):
    minNum = min(l[i])
    result = max(result, minNum)

print(result)