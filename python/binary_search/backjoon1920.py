n = int(input())
nums = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

for x in targets:
    result = 1 if x in nums else 0
    print(result)

