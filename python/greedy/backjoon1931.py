n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort(key=lambda x: (x[1], x[0]))

result = 0
nextTime = 0
for start, end in array:
    if start >= nextTime:
        result += 1
        nextTime = end
print(result)