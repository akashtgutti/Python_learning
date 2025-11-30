# Class Methods
# Methods are functions that belong to a class. They define the behavior of objects created from the class.
# This is a normal method that takes 'self' as the first parameter, which refers to the instance of the class.
# The actual class method is defined using the @classmethod decorator and takes 'cls' as the first parameter, which refers to the class itself.

class Bank:
    def __init__(self,account_type, bank_name):
        self.bank_name = bank_name
        self.account_type = account_type
        
    def bank_address(self):
        print("PCMC,pune,Maharashtra,India")
        
p1 = Bank("savings","SBI")
print(p1.bank_address())

# Methods with Parameters
# Methods can accept parameters just like regular functions:


class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))