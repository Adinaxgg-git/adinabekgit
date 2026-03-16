#Найти позицию первого максимального элемента.
n = int(input())
numbers = list(map(int, input().split()))

m = max(numbers)

print(numbers.index(m) + 1)
