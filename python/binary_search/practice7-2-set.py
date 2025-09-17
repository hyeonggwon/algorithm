n = int(input())
parts = set(map(int, input().split()))

m = int(input())
target_parts = list(map(int, input().split()))

for target in target_parts:
    if target in parts:
        print("yes", end=' ')
    else:
        print("no", end=' ')