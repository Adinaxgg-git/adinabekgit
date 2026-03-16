#Read an integer n and then n integers. Using map(), square each number and output the sum of all squares.


n=int(input())
numbers=list(map(int,input().split()))
squares=map(lambda x: x**2, numbers)
result=sum(squares)
print(result)
