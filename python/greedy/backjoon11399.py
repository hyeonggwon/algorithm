n = int(input())
P = list(map(int, input().split()))
P.sort()
sumP = 0
for i in range(len(P)):
    sumP += P[i] * (len(P) - i)
print(sumP)