from collections import Counter

def oper(arr):
    new_arr = []
    max_len = 0

    for row in arr:
        counter = Counter(x for x in row if x)

        pairs = sorted(counter.items(), key=lambda x: (x[1], x[0]))

        new_row = []
        for pair in pairs:
            new_row.extend(pair)

        new_row = new_row[:100]
        max_len = max(max_len, len(new_row))

        new_arr.append(new_row)

    for row in new_arr:
        while len(row) < max_len:
            row.append(0)

    return new_arr


r, c, k = map(int, input().split())
r -= 1
c -= 1

arr = [list(map(int, input().split())) for _ in range(3)]
time = 0

while time <= 100:

    # [r][c] == k 확인
    if r < len(arr) and c < len(arr[0]):
        if arr[r][c] == k:
            print(time)
            exit()

    if len(arr) >= len(arr[0]):
        arr = oper(arr)
    else:
        arr = list(map(list, zip(*arr)))
        arr = oper(arr)
        arr = list(map(list, zip(*arr)))

    time += 1

print(-1)