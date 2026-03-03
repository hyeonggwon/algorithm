import sys
input = sys.stdin.readline
stack = []
k = int(input())
for _ in range(k):
    x = int(input())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))