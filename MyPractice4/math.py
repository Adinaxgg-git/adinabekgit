import math
import random

# Built-in functions
print(min(3, 7, 1))
print(max(3, 7, 1))
print(abs(-10))
print(round(3.14159, 2))
print(pow(2, 3))

# Math module
print(math.sqrt(16))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pi)
print(math.e)

# Random module
print(random.random())
print(random.randint(1, 10))

names = ["Ali", "Dana", "Sara"]
print(random.choice(names))

random.shuffle(names)
print(names)
