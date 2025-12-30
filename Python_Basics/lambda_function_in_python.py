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
