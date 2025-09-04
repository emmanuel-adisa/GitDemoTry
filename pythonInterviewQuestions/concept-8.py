"""

    self is not a keyword but a convention in Python
    It refers to the current instance of a class
    It must be the first parameter in instance methods
    though you don't need to pass it explicitly when calling methods.

    Unlike some languages(like java or cc++), Python does not have an explicit this keyword. Instead self
    is used to access instance variables and methods inside the class

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old {self.greet()}"


person1 = Person("Alice", 30)

#Calling the instance method
print(person1.greet()) # Output: Hello, my name is Alice and I am 30 years old.


