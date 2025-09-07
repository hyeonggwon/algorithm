from collections import deque
testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    docs = []
    for i in range(len(priorities)):
        docs.append([i, priorities[i]])
    docs = deque(docs)
    result = 0
    while True:
        doc = docs.popleft()
        for i in range(len(docs)):
            if docs[i][1] > doc[1]:
                docs.append(doc)
                doc = []
                break
        if doc:
            result += 1
            if doc[0] == m:
                break
    print(result)