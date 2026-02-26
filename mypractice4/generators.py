# generators.py

# 1. Generator for squares up to N
def squares_upto(N):
    for i in range(N + 1):
        yield i ** 2

print(list(squares_upto(5)))  # Test example

# 2. Even numbers between 0 and n (comma separated)
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = 10
print(",".join(map(str, even_numbers(n))))

# 3. Numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print(list(divisible_by_3_and_4(20)))

# 4. Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for sq in squares(2, 5):
    print(sq)

# 5. Generator numbers from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print(list(countdown(5)))