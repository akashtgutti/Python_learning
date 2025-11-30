# Class Method
# Methods are functions that belong to a class. They define the behavior of objects created from the class.
# The actual class method is defined using the @classmethod decorator and takes 'cls' as the first parameter, 
# which refers to the class itself.
# A class method is bound to the class & receives the class as an implicit first argument.
# Note - static method can't access or modify class state & generally for utility.


# Method 1 t ochange class attribute

class Person:
    name = "John"
    
    def changename(self,name):
        Person.name = name

p1 = Person()
p1.name="akash"
print(p1.name)


# Method 2 to access class attribute

class Person1:
    name = "John"
    
    def changename(self,name):
        self.__class__.name = name

p1 = Person1()
name = p1.changename("akash")
print(name)

# Metod 3 to access and modify class attribute
# In class function only class method can access and modify class attribute.

class Person2:
    name = "John"
    
    @classmethod
    def changename(cls,name):
        cls.name = name

p2 = Person2()

print(p2.changename("Gutti"))



        