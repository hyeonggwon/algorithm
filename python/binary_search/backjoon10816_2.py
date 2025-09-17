m = int(input())
nums = list(map(int, input().split()))

n = int(input())
targets = list(map(int, input().split()))

counts = dict()
for n in nums:
    counts[n] = counts.get(n, 0) + 1

for target in targets:
    print(counts.get(target, 0), end=' ')