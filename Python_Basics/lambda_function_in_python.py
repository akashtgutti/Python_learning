# Lambda Functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))


x1 = lambda a, b : a * b
print(x1(5, 6))


x2 = lambda a, b, c : a + b + c
print(x2(5, 6, 2))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(11))


# Lambda with Built-in Functions
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# Using Lambda with map()
# The map() function applies a function to every item in an iterable:

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


# Using Lambda with filter()
# The filter() function creates a list of items for which a function returns True:

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers1))
print(odd_numbers)

# Using Lambda with sorted()
# The sorted() function can use a lambda as a key for custom sorting:

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

words1 = ["apple", "pie", "banana", "cherry"]
sorted_words1 = sorted(words1, key=lambda x: len(x), reverse=True)
print(sorted_words1)