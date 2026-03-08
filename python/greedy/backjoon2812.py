# 첫 번째 풀이 : 시작부분부터 queue에 집어넣으면서 최대값인 것만 빼서 answer에 넣는 식으로 풀이
# 시간복잡도 : O(n)
# 시간복잡도는 빠르지만, 매 스텝마다 최대값을 구하는 것으로 인해 1~10까지 순환함
# 따라서 stack을 활용한 풀이 방식보다 10배 느림
#
# from collections import deque
# import sys
#
# def get_max():
#     res = -1
#     for i in range(9, -1, -1):
#         if counts[i] > 0:
#             res = i
#             break
#     return res
#
# input = sys.stdin.readline
# N, K = map(int, input().split())
# nums = deque(map(int, list(input().rstrip())))
# counts = [0] * 10
# queue = deque()
#
# for _ in range(K):
#     num = nums.popleft()
#     counts[num] += 1
#     queue.append(num)
#
# answer = ''
# for i in range(K, N):
#     num = nums.popleft()
#     counts[num] += 1
#     queue.append(num)
#     max_num = get_max()
#     while queue:
#         x = queue.popleft()
#         counts[x] -= 1
#         if x == max_num:
#             break
#     answer += str(max_num)
# print(answer)

# 두 번째 풀이 : 숫자의 시작 부분부터 스택에 집어 넣기 전에,
# 스택 최상단의 값이 현재 숫자보다 작을 때 pop을 하고 K 값을 줄여나가는 식으로 풀이
# 맨 앞 자리부터 K개의 원소를 빼기만 하면 되고, 스택에 남은 건 본인보다 앞자리가 큰 게 없는 수이기 때문에 최댓값임
# 다만 예외처리로, 아직 빼지 않은 수 K가 뒤에 남아 있을 때, 뒷자리의 수를 남은 K만큼 빼면 됨
# 시간복잡도 : O(n)

import sys

def solution(K):
    for x in nums:
        while K > 0 and stack and stack[-1] < x:
            stack.pop()
            K -= 1
        stack.append(x)
    while K > 0:
        stack.pop()
        K -= 1
    print(''.join(map(str, stack)))

input = sys.stdin.readline
N, K = map(int, input().split())
nums = input().rstrip()
stack = []

solution(K)