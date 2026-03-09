import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [input().rstrip() for _ in range(n)]
    arr.sort()

    answer = 'YES'
    for i in range(n - 1):
        if len(arr[i]) <= len(arr[i + 1]):
            if arr[i + 1].startswith(arr[i]):
                answer = 'NO'
                break
    print(answer)