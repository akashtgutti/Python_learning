# Set
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

myset = {"apple", "banana", "cherry"}

print(myset)

# Itoms accessing in Set

for x in myset:
  print(x)
  
#Using while loop to access items in Set

myset = {"apple", "banana", "cherry"}

print( "app" in myset)


# Add an item to a set, using the add() method:

thisset2 = {"apple", "banana", "cherry"}

thisset2.add("orange")

print(thisset2)


# To add items from another set into the current set, use the update() method.
# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")

print(thisset)


# Union
# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
