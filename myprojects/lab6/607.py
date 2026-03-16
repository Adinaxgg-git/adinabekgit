#read an integer n and then n words. Using max(..., key=len), output the longest word. If several words have the same maximum length, output the first one.

n=int(input())
words=input().split()
longest=max(words,key=len)
print(longest)