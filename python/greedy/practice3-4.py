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
while n >= k:
    # Add operations for subtractions to make n divisible by k
    cnt += (n % k)
    n //= k
    # Add one operation for division
    cnt += 1

# Add remaining subtractions for n < k
if n > 1:
    cnt += (n - 1)
print(cnt)
