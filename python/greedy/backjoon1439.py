import sys
input = sys.stdin.readline().rstrip
s = list(map(int, list(input())))

cnt = [0, 0]
cnt[s[0]] += 1
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        cnt[s[i]] += 1

print(min(cnt))