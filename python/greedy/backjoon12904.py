import sys
input = sys.stdin.readline
s = list(input().rstrip())
t = list(input().rstrip())

'''
문자열 T에서 거꾸로 변환을 해가면서 문자열 S와 길이가 같아졌을 때,
변환한 T가 S와 똑같다면 1이고, 다르다면 0임
왜냐, S에서 T로의 변환은 A를 더하는 것과 뒤집고 B를 더하는 것 둘 중에 하나아기 때문임
따라서 결과값인 T에서 만약 A가 나오면 그냥 A를 빼고 B가 나오면 B를 빼고 뒤집기를 반복하는 것이 S로 돌아가는 최적의 수고,
만약 길이가 같은데도 S와 변환된 T가 다르면 T로는 S로 변환할 수 없는 것임 
'''
while len(s) < len(t):
    ch = t.pop()
    if ch == 'B':
        t.reverse()

print(int(s == t))