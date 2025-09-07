x = int(input())
size = 1
totalSum = 0
while totalSum + size < x:
    totalSum += size
    size += 1
x -= totalSum
if size % 2 == 1:
    left = size - x + 1
    right = x
else:
    left = x
    right = size - x + 1
print(left, right, sep='/')