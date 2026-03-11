import bisect
import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    LIS = [A[0]]
    for x in A[1:]:
        if x > LIS[-1]:
            LIS.append(x)
        else:
            idx = bisect.bisect_left(LIS, x)
            LIS[idx] = x
    return len(LIS)

print(solution())