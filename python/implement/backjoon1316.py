NOT_VISITED = 0
VISITING = 1
VISITED = 2

n = int(input())
notGroupCnt = 0
for _ in range(n):
    word = input()
    visitStateDic = dict()
    visitStateDic[word[0]] = VISITING
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            visitStateDic[word[i - 1]] = VISITED
        visitState = visitStateDic.get(word[i], NOT_VISITED)
        if visitState == NOT_VISITED:
            visitStateDic[word[i]] = VISITING
        elif visitState == VISITED:
            notGroupCnt += 1
            break
result = n - notGroupCnt
print(result)

