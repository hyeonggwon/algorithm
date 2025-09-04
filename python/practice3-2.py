N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
first = numbers[N - 1]
second = numbers[N - 2]

count = (M // (K + 1)) * K
count += M % (K + 1)

result = 0
result += count * first
result += (M - count) * second
print(result)