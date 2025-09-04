N, M, K = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
first = l[N - 1]
second = l[N - 2]

count = (M // (K + 1)) * K
count += M % (K + 1)

result = 0
result += count * first
result += (M - count) * second
print(result)