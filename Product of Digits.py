n = int(input())
product_digit = 1

while n > 0:
    last = n % 10
    product_digit *= last
    n = n // 10

print(product_digit)
