#Read an integer n, then n keys and n values. Build a dictionary using zip(keys, values). Then read one query key and output its value, or Not found if the key is absent.
n=int(input())
keys=input().split()
values=input().split()
d=dict(zip(keys,values))
query=input()
if query in d:
    print(d[query])
else:
    print("Not found")