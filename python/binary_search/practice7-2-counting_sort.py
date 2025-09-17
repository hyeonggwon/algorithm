n = int(input())
parts = list(map(int, input().split()))

m = int(input())
target_parts = list(map(int, input().split()))

MAX = 1_010_101
counts = [0] * (MAX + 1)

for i in parts:
    counts[i] += 1

for target in target_parts:
    if counts[target] > 0:
        print("yes", end=' ')
    else:
        print("no", end=' ')