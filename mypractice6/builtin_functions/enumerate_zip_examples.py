names = ["A", "B", "C"]
scores = [90, 85, 88]

# enumerate
for i, name in enumerate(names):
    print(i, name)

# zip
for name, score in zip(names, scores):
    print(name, score)

# type checking
x = "123"
print(type(x))

# conversion
y = int(x)
print(y, type(y))