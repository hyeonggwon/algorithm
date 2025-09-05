expList = list(input())
waitDigitStart = True
i = 0
isLeftParen = False
while i < len(expList):
    if expList[i] == '0' and waitDigitStart:
        del(expList[i])
        continue
    elif expList[i].isdigit():
        waitDigitStart = False
    else:
        waitDigitStart = True
        if expList[i] == '-':
            if isLeftParen:
                expList.insert(i, ')')
                isLeftParen = False
            else:
                expList.insert(i + 1, '(')
                i += 1
                isLeftParen = True
    i += 1
if isLeftParen:
    expList.append(')')

print(eval(''.join(expList)))