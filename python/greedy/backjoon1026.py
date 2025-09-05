n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

total_sum = 0
for i in range(n):
    total_sum += a[i] * b[i]
print(total_sum)