str = "RahulShettyAcademy.com"
str1 = "Consulting Firm"
str3 = "RahulShetty"



print(str[1]) #a
print(str[0:5]) #if you want substring in python

print(str + " " + str1)

print(str3 in str) #subsrting check

var = str.split(".")
print(var)
print(var[0])
str4 = " great "
print(str4.strip())
print(str4.lstrip()) # strip left side
print(str4.rstrip()) # strip right side
