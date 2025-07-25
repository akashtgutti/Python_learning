# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

a = ("akash", 34,34, 56, 78,78, "Gutti", 3.5, True, False)
print(a)

print(len(a))

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
B = ("apple",)
print(B)
print(type(B))

# Access Tuple Items
print(a[0])
print(a[1:5])

#Negative Indexing
print(a[-1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

X=(12,56,34,"Akash")
Y=list(X)
print(Y)
Y[0] = "45"
print(Y)
X = tuple(Y)
print(X)

#Unpacking a Tuple
a3 = ("apple", "banana", "cherry")
(C1, C2, C3) = a3
print(C1,C2,C3)


""" 
----Using Asterisk*-------

If the number of variables is less than the number of values, you can add an * to the variable name and 
the values will be assigned to the variable as a list

"""
Z1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
(C1, C2, *C3) = Z1
print(C1, C2, C3)

#Loop through a Tuple accessing the values one by one

for v in Z1:
    print(v)
    
for i in range(len(Z1)):
    print(Z1[i])
    
    
