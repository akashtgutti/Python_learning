# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) 
# to inherit attributes and methods from another class (called a parent or base class).
# In this article, we'll explore inheritance in Python.

# Type of Inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance



class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info()      # Inherited method
d.sound()

#This is single inheritance example
class Car:
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("Car stopped")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

Car1 = ToyotaCar("fortuner")
Car2 = ToyotaCar("innova")

print(Car1.start())


#Multi-level Inheritance

class GrandParent:
    def grandparent_method(self):
        print("This is the grandparent method.")
class Parent(GrandParent):
    def parent_method(self):
        print("This is the parent method.")
class Child(Parent):
    def child_method(self):
        print("This is the child method.")
c = Child()
c.grandparent_method()  # Inherited from GrandParent


#Multiple Inheritance

class Father:
    def father_method(self):
        print("This is the father method.")
class Mother:
    def mother_method(self):
        print("This is the mother method.")
class Child(Father, Mother):
    def child_method(self):
        print("This is the child method.")
c = Child()
c.father_method()  # Inherited from Father


# Super method
# Super method used to call the parent class method from the child class.


class Car1:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started .. ")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar1(Car1):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar1("prius", "electric")
print(car1.type)
