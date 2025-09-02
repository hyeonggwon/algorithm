n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

a = [1, 9, 5, 4]
a.insert(2, 3)
print(a)

a = [1, 2,  3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

answer = 7
print(f"정답은 {answer}입니다.")

# sorted에 람다 함수 추가
result = sorted([('홍길동', 36), ('이순신', 75), ('아무개', 50)], key=lambda x: x[1], reverse=True)
print(result)

# itertools 사용 - permutations(순열) : n 개의 데이터 중 r개를 뽑아 순서대로 나열하는 경우 계산
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# itertools 사용 - combinations(조합) : n 개의 데이터 중 r개를 뽑아 순서 고려하지 않고 나열하는 경우 계산
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# itertools 사용 - product(중복순열) : n 개의 데이터 중 r개를 뽑아 순서대로 나열하는 경우 계산, 중복 포함
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

# 오름차순 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8 ,0])
print(result)

# 내림차순 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8 ,0])
print(result)

# bisect : 정렬된 배열에서 특정한 원소를 찾을 때
# bisect_left(a,x) : 정렬된 순서를 유지하면서 리스트 a에 x를 넣을 수 있는 가장 왼쪽 인덱스
# bisect_right(a,x) : 정렬된 순서를 유지하면서 리스트 a에 x를 넣을 수 있는 가장 오른쪽 인덱스
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# bisect 이용해서 count_by_range 함수 구현 가능
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 3, 4))
print(count_by_range(a, -1, 3))

# deque : 큐, 스택 구현
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(list(data))

# Counter : 원소 개수
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))

# math 라이브러리
import math

print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21, 14))
print(math.pi)
print(math.e)