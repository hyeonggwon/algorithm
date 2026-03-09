import sys

input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    line = list(map(int, input().split()))
    A.append(line[0])
    B.append(line[1])
    C.append(line[2])
    D.append(line[3])

sums_AB = []
sums_CD = []
for i in range(n):
    for j in range(n):
        sums_AB.append(A[i] + B[j])
        sums_CD.append(C[i] + D[j])

sums_AB.sort()
sums_CD.sort()

length = n ** 2
left = 0
right = length - 1
answer = 0
while 0 <= left < length and 0 <= right < length:
    current_sum = sums_AB[left] + sums_CD[right]
    if current_sum == 0:
        next_left = left + 1
        while next_left < length and sums_AB[left] == sums_AB[next_left]:
            next_left += 1
        next_right = right - 1
        while next_right >= 0 and sums_CD[right] == sums_CD[next_right]:
            next_right -= 1
        answer += (next_left - left) * (right - next_right)
        left = next_left
        right = next_right
    elif current_sum < 0:
        left += 1
    else:
        right -= 1
print(answer)