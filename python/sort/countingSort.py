array = [7, 5, 9, 0, 3, 6, 2, 9, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for x in array:
    count[x] += 1

result = []
for i in range(len(count)):
    result += [i] * count[i]

print(result)