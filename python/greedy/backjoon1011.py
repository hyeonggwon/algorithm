import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x

    top = int(dist ** 0.5)

    dist -= top ** 2
    plus = dist // top
    remainder = dist % top
    if remainder != 0: plus += 1
    print(2 * top - 1 + plus)