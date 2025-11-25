#All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

#The __init__() method is used to assign values to object properties, or to perform operations that are necessary 
# when the object is being created.

# The __init__() method is called automatically every time the class is being used to create a new object.

class Myclass:
    def __init__(self,name,age):
        self.name = name
        self.age= age
        
Obj = Myclass("Akash",50)

print(Obj.name)
print(Obj.age)

print(Obj)
print(Myclass)