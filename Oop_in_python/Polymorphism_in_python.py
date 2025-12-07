# What is Polymorphism?
# The literal meaning of polymorphism is the condition of occurrence in different forms.
# Polymorphism is a very important concept in programming. It refers to the use of a single type entity
# (method, operator or object) to represent different types in different scenarios.

# Example 1: Polymorphism in addition operator
# We know that the + operator is used extensively in Python programs. But, it does not have a single usage.

# For integer data types, + operator is used to perform arithmetic addition operation.

num1 = 1
num2 = 2
print(num1+num2)


# Similarly, for string data types, + operator is used to perform concatenation
str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

# Class Polymorphism in Python
# Polymorphism is a very important concept in Object-Oriented Programming.

# To learn more about OOP in Python, visit: Python Object-Oriented Programming

# We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name.

# We can then later generalize calling these methods by disregarding the object we are working with. Let's look at an example:

# Example 3: Polymorphism in Class Methods

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

# Here, we have created two classes Cat and Dog. They share a similar structure and have the same method names info() and make_sound().

# However, notice that we have not created a common superclass or linked the classes together in any way. 
# Even then, we can pack these two different objects into a tuple and iterate through it using a common animal variable. 
# It is possible due to polymorphism.

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


