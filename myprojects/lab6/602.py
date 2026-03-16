#Read an integer n and then n integers. Using filter(), keep only even numbers and output how many there are.

n=int(input())
numbers=list(map(int,input().split()))
even=filter(lambda x: x%2==0, numbers)
print(len(list(even)))

