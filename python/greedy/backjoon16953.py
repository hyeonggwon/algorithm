a, b = map(int, input().split())
arr = []
while True:
    arr.append(b)
    if b != 1 and b % 10 == 1:
        b -= 1
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        break

result = -1
for i in range(len(arr)):
    if arr[i] == a:
        result = i + 1
print(result)