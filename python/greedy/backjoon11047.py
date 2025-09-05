n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

result = 0

for i in range(n - 1, -1, -1):
    result += k // A[i]
    k %= A[i]

print(result)