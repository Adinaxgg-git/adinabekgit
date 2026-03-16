#Read an integer n , then two  A arrays B and  of length f . Using zip(), compute and output the dot product
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
result=0
for a,b in zip(A,B):
    result=result+a*b
print(result)