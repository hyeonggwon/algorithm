def solution(S):
    # Implement your solution here
    if len(S) % 2 == 0:
        return -1
    if len(S) == 1:
        return 0
    mid = len(S) // 2
    left = 0
    right = len(S) - 1
    while 0 <= left < mid and mid < right <= len(S) - 1:
        if S[left] != S[right]:
            return -1
        left += 1
        right -= 1
    return mid