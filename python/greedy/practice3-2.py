N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

first_largest = numbers[-1]
second_largest = numbers[-2]

# Number of times the repeating block (K times first, 1 time second) is used
num_blocks = M // (K + 1)
# Number of remaining additions, which will be the largest number
remainder = M % (K + 1)

result = num_blocks * (first_largest * K + second_largest) + remainder * first_largest

print(result)