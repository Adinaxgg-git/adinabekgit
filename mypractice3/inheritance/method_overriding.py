# method_overriding.py

class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()
