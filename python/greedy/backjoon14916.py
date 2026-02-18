import sys

input = sys.stdin.readline
n = int(input())

'''
2와 5의 최소공약수는 10.
5를 가장 많이 더할 수록 최솟값
따라서,
1. 5를 최대한 많이 더한 후 남은 2를 더한 횟수
만약 1번에서 딱 떨어지지 않는다면
2. 1번에서 5를 -1 만큼 더한 후 남은 2를 더한 횟수
가 최소가 된다. 
'''
result = -1
for i in range(2):
    # 5를 최대한 많이 더한 횟수
    a = n // 5 - i
    # 남은 수를 2로 나눈 수
    b = (n - a * 5) // 2
    if a <= -1:
        # 음수 방지
        result = -1
        break
    if (n - a * 5) % 2 == 0:
        # 딱 맞아 떨어질 때 result 값 계산
        result = a + b
        break

print(result)
