n = int(input())
result = 0
for _ in range(n):
    word = input()
    check = [False] * 26
    prevX = ''
    isGroup = True
    for x in word:
        i = ord(x) - ord('a')
        if check[i] and x != prevX:
            isGroup = False
            break
        check[i] = True
        prevX = x
    if isGroup:
        result += 1
print(result)