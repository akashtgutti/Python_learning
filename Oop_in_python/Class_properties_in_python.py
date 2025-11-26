# Class Properties
# Properties are variables that belong to a class. They store data for each object created from the class.
class Car:
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name
        

p1 = Car("Red", "BMW")

print(p1.colour)
    

# Access Properties
# You can access object properties using dot notation.

class Car1:
      def __init__(self, brand, model):
          self.brand = brand
          self.model = model

car2 = Car1("Toyota", "Corolla")

print(car2.brand)
print(car2.model)


# Modify Properties
# You can modify the value of properties on objects:

class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)