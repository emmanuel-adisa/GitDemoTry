"""
    A Lambda function in Python is a small, anonymous function
    that can have multiple arguments but only one expression.

    It is written in a single line.
    It is used where a short function is needed temporarily.
        Don't use lambda if the function is complex-use def instead

"""

def add(x,y):
    return x + y


add = lambda x, y : x + y


numbers = [1, 2, 3, 4 ,5]

# for i in numbers:
#     i = i * 2
#     print(i)

squared_numbers = map(lambda x : x*2, numbers)

print(list(squared_numbers))

even_numbers = list(filter(lambda x: x % 2 == 0,numbers))
print(even_numbers)

num = [3, 2, 6, 1]

print(num[::-1])
print(sorted(num))


