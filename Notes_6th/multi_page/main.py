#Vienna LaRose, Multiple Python pages notes

#1. How do you make multiple files in python?
    #Make a new file ending in .py 
    #snake case file names 
    #descriptive file names (short)

#2. How do you get a function from another file
from calc import addition as add, subtraction as sub
    #alising is where you import a function and give it a new keyword


print(add())


#3. How do you get variables from another file?
from calc import num

print(sub(num,8))
#better to return from a function

#4. How do you have a function with multiple returns?
def get_user_info():
    name = input("What is your name\n")
    quest = input("What is your quest\n")
    color = input("What is your favorite color\n")
    return name, quest, color

name, quest, color = get_user_info()

print(quest)

#5. Why would you use multiple pages for a python project? 
    #Easier to merge github branches
    #Modularity - breaking the program into smaller more managable pieces. 
    #functionality - keeps your code clean 