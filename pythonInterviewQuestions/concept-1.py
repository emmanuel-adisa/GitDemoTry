#Lists are mutabl, tuples are immutable

my_list = [1, 2, 3]

my_list[0] = 100

my_list.append(4) # [100, 2, 3, 4]

my_list.pop(1)
print(my_list)


my_tuple = (1, 2, 3)
#my_tuple[0] = 100 - Not allowed
# my_tuple[0] = 3
print(my_tuple)


x = 10 #int
y=3.14 #float
d = {"a": 1} #dictionary key value pairs
s = "hello"
z = True
my_list = [1, 2, 3] #list
my_tuple = (1, 2, 3) #tuple

