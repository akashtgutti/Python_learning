class MyfirstClass:
    X = 5

print(MyfirstClass)

X1 = MyfirstClass()
X2 = MyfirstClass()
print(X1.X)
print(X1)

#How to delete a object

del X2
#print(X2)   This will raise an error since X2 has been deleted


#You can create multiple objects from the same class:
p1 = MyfirstClass()
p2 = MyfirstClass()
p3 = MyfirstClass()

print(p1.X)
print(p2.X)
print(p3.X)

#pass Statement :-
#class definitions cannot be empty, but if you for some reason have a class definition
# with no content, put in the pass statement to avoid getting an error.
class Person:
    pass
