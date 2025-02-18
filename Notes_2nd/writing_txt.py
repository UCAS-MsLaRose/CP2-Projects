
"""
r= read (won't create a file)
w= write (won't create a file)
w+ = read and write (won't create a file)
a = append (add things but not write over) (Will create the file if it isn't there)
x = create a file
"""
with open('Notes_2nd/things.txt', "w+") as file:
    file.write("This is now my file")
    print(file.read())

with open('Notes_2nd/things.txt', "a+") as file:
    file.write("\nI just made another line on my file!")

with open('Notes_2nd/things.txt', "r") as file:
    print(file.read())