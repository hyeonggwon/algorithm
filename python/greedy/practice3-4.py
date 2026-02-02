# n, k = map(int, input().split())
# result = 0
# while True:
#     if n == n % k:
#         break
#     result += n % k
#     n -= n % k
#     result += 1
#     n //= k
# result += n - 1
# print(result)




















n, k = map(int, input().split())
cnt = 0
while n > 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    cnt += 1
print(cnt)
