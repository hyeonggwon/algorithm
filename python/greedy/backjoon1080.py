import sys

'''
행렬을 왼쪽 위부터 점검한다고 할 때, (i, j)를 왼쪽 위로하는 3 x 3 행렬 뒤집기 변환이 있다고 하자.
그럼 (i, j)가 다를 때 뒤집는 게 최선의 수임
왜냐, (i + 1, j) 나 (i, j + 1) 등에서 행렬 변환을 한다면 이미 지나간 자리 (i, j)는 어떤 수를 써도 변환할 수가 없기 때문임
따라서 왼쪽 위부터 점검을 하면서 (i, j)가 다를 때 행렬 변환을 하는 것이 강제적이며 가장 최선안 수임
'''

# 행렬 변환 함수
def operation(i, j, matrix):
    for k in range(0, 3):
        for l in range(0, 3):
            matrix[i + k][j + l] = (matrix[i + k][j + l] + 1) % 2

input = sys.stdin.readline
n, m = map(int, input().split())
matrix1 = [list(map(int, list(input().rstrip()))) for _ in range(n)]
matrix2 = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# 행렬을 왼쪽 위부터 점검하면서, (i, j)가 다를 때 행렬 변환
result = 0
for i in range(n - 2):
    for j in range(m - 2):
        if matrix1[i][j] != matrix2[i][j]:
            operation(i, j, matrix1)
            result += 1

# 두 행렬이 다르면 -1 (예외처리)
if matrix1 != matrix2:
    result = -1

print(result)