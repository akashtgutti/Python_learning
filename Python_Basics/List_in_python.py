#LIST is mutable we can change the values

#In a LIST we can pass multiple data type values like String, float and integer


a=["akash",34,56,78,"Gutti",3.5,True,False]
print(a)

print(a[0])

print(a[:5])

a[0] = "Shivani"

print(a)

a.insert(1,33)
print(a)

a.append("Kalu")

print(a)

b = ["SK","ddf","dfd","dfd"]

a.extend(b)
print(a)

# Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist.pop()
print(thislist)


# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist


# Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)



# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

