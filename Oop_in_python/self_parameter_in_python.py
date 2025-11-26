# The self Parameter
# The self parameter is a reference to the current instance of the class.

# It is used to access properties and methods that belong to the class.

class Technology:
    def __init__(self,IT,Electronics):
        self.IT = IT
        self.Electronics = Electronics
        
    def selectTech(self):
        print(f"This technology you slected : {self.IT}")
        print(f"This technology you slected : {self.Electronics}")
        
Obj = Technology("AI","IoT")
print(Obj.selectTech())