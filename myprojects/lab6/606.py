#Read an integer n and then n integers. Using all(), check whether every number is non-negative. Print Yes or No.
n=int(input())

numbers=list(map(int,input().split()))

if all(x>=0 for x in numbers):
    print("Yes")
else:
    print("No")