n, k = map(int, input().split())
result = 0
while True:
    if n == n % k:
        break
    result += n % k
    n -= n % k
    result += 1
    n //= k
result += n - 1
print(result)