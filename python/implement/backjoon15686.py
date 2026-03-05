import itertools
import sys

def solution():
    INF = sys.maxsize
    input = sys.stdin.readline
    n, m = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(n)]
    house_pos = []
    chick_pos = []

    for i in range(n):
        for j in range(n):
            if total_map[i][j] == 1:
                house_pos.append((i, j))
            elif total_map[i][j] == 2:
                chick_pos.append((i, j))

    selected_chick_pos = itertools.combinations(chick_pos, m)
    result = INF
    for l in selected_chick_pos:
        dist_sum = 0
        for h_x, h_y in house_pos:
            chick_dist = INF
            for c_x, c_y in l:
                chick_dist = min(chick_dist, abs(h_x - c_x) + abs(h_y - c_y))
            dist_sum += chick_dist
        result = min(result, dist_sum)

    print(result)

solution()