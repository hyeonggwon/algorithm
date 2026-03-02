import sys

# 시간복잡도 : O(n)

input = sys.stdin.readline
n, l = map(int, input().split())
holes = list(map(int, input().split()))

# 우선 구멍들을 정렬
holes.sort()

# 구멍의 시작부분부터 길이 L로 채울 수 있는 부분들을 최대한 채워나감
# start는 테이프를 다 쓸 때마다 다음 구멍의 위치임
start = holes[0]
result = 0
for i in range(1, len(holes)):
    # 시작점으로부터 구멍까지의 길이가 테이프의 길이보다 짧을 때
    if holes[i] - start <= l - 1:
        continue
    # 시작점으로부터 구멍까지의 길이가 테이프의 길이를 넘어설 때, start 갱신 및 result 값 더하기
    else:
        start = holes[i]
        result += 1
result += 1

print(result)