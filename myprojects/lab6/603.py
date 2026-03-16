#Read an integer n and then n words. Using enumerate(), output pairs in the format index:word, separated by one space.
n=int(input())
words=input().split()
for i, word in enumerate(words):
    print(f"{i}:{word}", end=" ")
