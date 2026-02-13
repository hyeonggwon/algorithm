import sys

def solution(n):
    if '0' not in n:
        return '-1'
    total_sum = 0
    for i in n:
        total_sum += int(i)
    if total_sum % 3 != 0:
        return '-1'
    n.sort(reverse=True)
    return ''.join(n)

input = sys.stdin.readline().rstrip
n = list(input())

print(solution(n))