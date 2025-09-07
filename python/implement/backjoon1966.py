from collections import deque
testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    docs = deque(enumerate(priorities))
    result = 0
    while True:
        doc = docs.popleft()
        if any(d[1] > doc[1] for d in docs):
            docs.append(doc)
        else:
            result += 1
            if doc[0] == m:
                break
    print(result)