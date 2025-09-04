class MyClass:
    @classmethod
    def class_method(cls):
        return "Class"



    def instance_method(self):
        return "Instance"


# obj = MyClass()

# print(obj.class_method()) # Instance
print(MyClass.class_method()) # Class