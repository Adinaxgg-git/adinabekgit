#Проверить, является ли число степенью двойки (через цикл).
n=int(input())
x=1
while x<n:
    x=x*n
if x==n:
    print("Yes")
else:
    print("No")