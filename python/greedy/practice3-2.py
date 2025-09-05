N, M, K = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
first = l[N - 1]
second = l[N - 2]

result = 0

result += first * K * (M // (K + 1))
result += second * (M // (K + 1))

M -= (M // (K + 1)) * (K + 1)

result += first * M
print(result)