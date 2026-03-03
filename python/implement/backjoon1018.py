import sys

def count(i, j):
    w_first = list('WBWBWBWB')
    b_first = list('BWBWBWBW')

    cases = [[w_first, b_first] * 4, [b_first, w_first] * 4]
    cases_cnt = [0, 0]

    for t in range(2):
        for k in range(8):
            for l in range(8):
                if arr[i + k][j + l] != cases[t][k][l]:
                    cases_cnt[t] += 1

    return min(cases_cnt)

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

result = sys.maxsize
for i in range(n - 7):
    for j in range(m - 7):
        result = min(result, count(i, j))

print(result)