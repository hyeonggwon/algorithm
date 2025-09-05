n, k = map(int, input().split())
A = list()
for _ in range(n):
    A.append(int(input()))

result = 0

for i in range(n - 1, -1, -1):
    result += k // A[i]
    k %= A[i]

print(result)