import sys

input = sys.stdin.readline

r,c = map(int,input().split())
graphs = [[] for _ in range(r)]
for i in range(r):
    graphs[i] = input().strip()

ans = 1
targets = set([(0, 0, graphs[0][0])])
moves = [[1,0],[-1,0],[0,1],[0,-1]]

while targets:
    x,y,temp_target = targets.pop()
    ans = ans if ans > len(temp_target) else len(temp_target)

    if ans == 26:
        break

    for dx,dy in moves:
        target_x, target_y = x + dx, y + dy
        if 0 <= target_x < r and 0 <= target_y < c:
            next_target = graphs[target_x][target_y]
            if next_target not in temp_target:
                targets.add((target_x,target_y,temp_target + next_target))

print(ans)