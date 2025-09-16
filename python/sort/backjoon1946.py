import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    array = [tuple(map(int, input().split())) for _ in range(n)]
    second_rank_array = [0] * (n + 1)

    for x in array:
        second_rank_array[x[0]] = x[1]

    result = 1
    min_interview_rank = second_rank_array[1]
    for i in range(2, len(second_rank_array)):
        if second_rank_array[i] < min_interview_rank:
            min_interview_rank = second_rank_array[i]
            result += 1
    print(result)


