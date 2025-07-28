# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

print(thisdict["brand"])

print(thisdict.keys())

print(thisdict.values())

thisdict["brand"] = "Mahindra"

print(thisdict)


# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2["color"] = "red"
print(thisdict2)

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. 
# If the item does not exist, the item will be added.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"chassi no":"MS-12-45-67"})

print(thisdict)
