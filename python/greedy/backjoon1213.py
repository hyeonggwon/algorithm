import sys
import collections

# 글자수가 짝수일 때 -> 2로 나눈 몫의 개수만큼 left에 넣기 (나중에 right에 반대로 채우면 되니까)
# 글자수가 홀수일 때 -> 2로 나눈 몫의 개수만큼 left에, 하나는 middle에 넣기 (단, 글자수가 홀수인 게 1개보다 많으면 팰린드롬 불가)
def solution():
    counter = collections.Counter(name)
    left = ""
    middle = ""
    # 알파벳 A 부터 Z까지 순회
    for x in range(ord('A'), ord('Z') + 1):
        # 알파벳이 존재할 때
        if counter.get(chr(x)):
            # 글자수가 홀수일 때
            if counter.get(chr(x)) % 2 == 1:
                # 글자수가 홀수인 게 이미 있을 때
                if middle:
                    return "I'm Sorry Hansoo"
                # 글자수가 홀수인 게 없었을 때
                else:
                    middle = chr(x)
            # 2로 나눈 몫의 개수만큼 left에 넣기
            left += chr(x) * (counter.get(chr(x)) // 2)
    # left + middle + right
    return left + middle + left[::-1]

input = sys.stdin.readline().rstrip
name = input()

print(solution())