# Getter and Setter in Python

# In Python, a getter and setter are methods used to access and update the attributes of a class. 
# These methods provide a way to define controlled access to the attributes of an object, thereby ensuring the integrity of the data. 
# By default, attributes in Python can be accessed directly. However, this can pose problems when attributes need validation or 
# transformation before being assigned or retrieved.

# Getter: The getter method is used to retrieve the value of a private attribute. It allows controlled access to the attribute.
# Setter: The setter method is used to set or modify the value of a private attribute. It allows you to control how the value is 
# updated, enabling validation or modification of the data before it’s actually assigned.


#Getters and setters using normal method

class Geek: 
	def __init__(self, age = 0): 
		self._age = age 
	
	# getter method 
	def get_age(self): 
		return self._age 
	
	# setter method 
	def set_age(self, x): 
		self._age = x 

raj = Geek() 

# setting the age using setter 
raj.set_age(21) 

# retrieving age using getter 
print(raj.get_age()) 

print(raj._age)

#Getters and setters using property() function

class Geeks: 
	def __init__(self): 
		self._age = 0
	
	# function to get value of _age 
	def get_age(self): 
		print("getter method called") 
		return self._age 
	
	# function to set value of _age 
	def set_age(self, a): 
		print("setter method called") 
		self._age = a 

	# function to delete _age attribute 
	def del_age(self): 
		del self._age 
	
	age = property(get_age, set_age, del_age) 

mark = Geeks() 

mark.age = 10

print(mark.age)

