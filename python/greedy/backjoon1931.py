n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort(key=lambda x: (x[1], x[0]))

result = 0
nextTime = 0
for i in range(len(array)):
    if array[i][0] >= nextTime:
        result += 1
        nextTime = array[i][1]
print(result)