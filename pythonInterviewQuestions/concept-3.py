with open("test.txt","w") as f:
    f.write("Hello World!")

try:
    with open("test.txt", "r") as f:
        content = f.read()
        print(content)


except Exception as e:
    print(e)

finally: # will execute irrespective if test fails
    print("close database connection, clean up resources")

