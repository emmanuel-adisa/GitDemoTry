file = open('test.txt')
#read all the contents of file
#read a number of characters by passing parameter
#print(file.read(5))
#read one single line at a time readline()
#
# print(file.readline())
# print(file.readline())
# file.close()

#print line by line using readline method

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()
#


#values = [abc, bvdsf, cat, dog, elephant]
for line in file.readlines():
    print(line)
