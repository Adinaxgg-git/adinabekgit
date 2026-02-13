# class_variables.py

class Dog:
    species = "Canine"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

d1 = Dog("Buddy")
d2 = Dog("Max")

print(d1.species)
print(d2.name)
