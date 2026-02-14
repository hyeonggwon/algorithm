n, m = map(int, input().split())
min_price_package = float('inf')
min_price_one = float('inf')

for _ in range(m):
    price_package, price_one = map(int, input().split())
    min_price_package = min(min_price_package, price_package)
    min_price_one = min(min_price_one, price_one)

min_price_package = min(min_price_package, min_price_one * 6)

result = min_price_package * (n // 6)
if n % 6 != 0:
    result += min(min_price_package, min_price_one * (n % 6))

print(result)