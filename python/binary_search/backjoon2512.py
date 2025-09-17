import sys

def binary_search(start, end):
    result = 1
    while start <= end:
        mid = (start + end) // 2
        sum_budgets = 0
        for budget in budgets:
            sum_budgets += min(budget, mid)
        if sum_budgets > m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

input = sys.stdin.readline
n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

start = 0
end = max(budgets)

print(binary_search(start, end))