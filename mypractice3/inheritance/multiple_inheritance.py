# multiple_inheritance.py

class Father:
    def skill(self):
        print("Driving")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skill()
child.talent()
