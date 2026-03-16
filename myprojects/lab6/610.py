#Read an integer n  and then n integers. Using map() with bool and sum(), count how many numbers are truthy (non-zero).
n = int(input())

numbers = list(map(int, input().split()))

result = sum(map(bool, numbers))

print(result)
