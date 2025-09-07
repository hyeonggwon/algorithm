import copy
from itertools import combinations

n, m = map(int, input().split())
totalMap = [list(map(int, input().split())) for _ in range(n)]
virusPos = [(i, j) for i in range(n) for j in range(m) if totalMap[i][j] == 2]
virusCnt = 0
wallCnt = 0
for line in totalMap:
    for item in line:
        if item == 1:
            wallCnt += 1
maxSafetyAreaCnt = 0

def spreadVirus(i, j, virtualMap):
    global virusCnt
    virtualMap[i][j] = 2
    virusCnt += 1
    if i - 1 >= 0 and virtualMap[i - 1][j] == 0:
        spreadVirus(i - 1, j, virtualMap)
    if i + 1 < n and virtualMap[i + 1][j] == 0:
        spreadVirus(i + 1, j, virtualMap)
    if j - 1 >= 0 and virtualMap[i][j - 1] == 0:
        spreadVirus(i, j - 1, virtualMap)
    if j + 1 < m and virtualMap[i][j + 1] == 0:
        spreadVirus(i, j + 1, virtualMap)

empty_spaces = [(r, c) for r in range(n) for c in range(m) if totalMap[r][c] == 0]

for wall_positions in combinations(empty_spaces, 3):
    virtualMap = copy.deepcopy(totalMap)
    for r, c in wall_positions:
        virtualMap[r][c] = 1
    virtualWallCnt = wallCnt + 3
    virusCnt = 0
    for i, j in virusPos:
        spreadVirus(i, j, virtualMap)
    safetyAreaCnt = n * m - virtualWallCnt - virusCnt
    maxSafetyAreaCnt = max(maxSafetyAreaCnt, safetyAreaCnt)
print(maxSafetyAreaCnt)