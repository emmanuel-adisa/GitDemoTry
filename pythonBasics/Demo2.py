
values = [1, 2, "Rahul", 4, 5]
#List is a data type that allows multiple values and can be different data types

print(values[0])

print(values[3])

print(values[-1])

print(values[1:3])

values.insert(3, "shetty") # [1, 2, 'Rahul', 'shetty', 4, 5]
print(values)

values.append("End") #[1, 2, 'Rahul', 'shetty', 4, 5, 'End']
print(values)

values[2] = "RAHUL" # Updating

del values[0]
print(values)

#Tuple - `Same as LIST data type but immutable (updation is not possible)
val = (1, 2, "rahul", 4.5)

print(val[1])
#val[2] = "RAHUL"
print(val)

# Dictionary

dic = {"a": 2, 4:"bcd", "c": "Hello World"}

print(dic[4])
print(dic["c"])

dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "Shetty"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])