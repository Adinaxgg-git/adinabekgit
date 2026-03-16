#Вывести все степени двойки ≤ n.
n=int(input())
x=1
while x<=n:
    print(2**x,end=" ")
    x=x+1