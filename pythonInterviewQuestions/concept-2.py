class Parent:
    def greet(self):
        return "Hello from Parent"


class Child(Parent):
    def __init__(self,title):
        self.title = title

    def greet(self):
        return super().greet()+"Hello from child class"+self.title




c = Child("rahulshettyacademy")
print(c.greet())
