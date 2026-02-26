# -------------------------------
# ITERATOR EXAMPLE
# -------------------------------

numbers = [1, 2, 3, 4]

my_iter = iter(numbers)

print(next(my_iter))
print(next(my_iter))


# -------------------------------
# CUSTOM ITERATOR
# -------------------------------

class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration

my_class = MyNumbers()
for x in my_class:
    print(x)


# -------------------------------
# GENERATOR FUNCTION
# -------------------------------

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


# -------------------------------
# GENERATOR EXPRESSION
# -------------------------------

squares = (x*x for x in range(5))
for s in squares:
    print(s)
