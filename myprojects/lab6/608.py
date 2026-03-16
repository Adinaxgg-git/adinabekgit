#Read an integer n  and then n integers. Using set() and sorted(), print all distinct numbers in increasing order, separated by spaces.

n=int(input())
numbers=list(map(int,input().split()))
unique=set(numbers)
sorted_numbers=sorted(unique)
print(*sorted_numbers)