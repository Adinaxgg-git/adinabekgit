#Подсчитать количество положительных чисел.
n=int(input())
num=list(map(int,input().split()))
count=0
for x in num:
    if x>0:
        count=count+1
print(count)