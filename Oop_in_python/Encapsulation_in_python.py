# Encapsulation means hiding internal details of a class and only exposing what’s necessary.
# It helps to protect important data from being changed directly and keeps the code secure and organized.

# This example shows encapsulation by keeping __salary variable private inside Employee class. 
# It cannot be accessed directly from outside the class.

# Private attributes and methods
# COnceptual Implementations in Python.
#Private attributes and methods are those that are intended to be accessed only within the class itself.
# In Python, we can indicate that an attribute or method is private by prefixing its name with double underscores (__).

class employee:
    def __init__(self, name, salary):
        self.name = name          # Public attribute
        self.__salary = salary    # Private attribute

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.__salary}")  # Accessing private attribute within the class

    def __calculate_bonus(self):  # Private method
        return self.__salary * 0.10

    def show_bonus(self):
        bonus = self.__calculate_bonus()  # Accessing private method within the class
        print(f"Employee Bonus: {bonus}")
        
emp = employee("John Doe", 50000)
print(emp.display_info())
print(emp.show_bonus())     


class person:
    __name = "Alice"  # Private class attribute
    
p1=person()
print(p1.__name)