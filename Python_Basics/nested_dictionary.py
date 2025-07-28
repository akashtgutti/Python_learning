# # Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


print(myfamily["child3"]["year"])

# Loop Dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  
  
for x in thisdict.values():
  print(x)
  

# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)