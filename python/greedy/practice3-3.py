# n, m = map(int, input().split())
# result = 0
# for _ in range(n):
#     row = list(map(int, input().split()))
#     result = max(result, min(row))
#
# print(result)






















n, m = map(int, input().split())
result = 0
for _ in range(n):
    result = max(result, min(map(int, input().split())))
print(result)