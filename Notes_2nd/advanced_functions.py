#Vienna LaRose, Advanced Notes Functions

# 1. What is a helper function?
    #Function called inside of a funciton to complete part of the task
def check_input(user_txt):
    return not any(char.isdigit() for char in user_txt)

def hello(name):
    if check_input(name):
        print(f"Hello {name}!")
    else:
        print("Please only input letters.")
        user = input("What is your name:\n").strip().capitalize()
        # 8. What is recursion?
            #when you call a function inside of itself
        hello(user)
        # 9. How does recursion work?
            #The function runs itself again

user = input("What is your name:\n").strip().capitalize()
hello(user)
# 2. What is the purpose of a helper function?
    #To make your fuctions simple 

# 3. What is an inner function?
    #A function defined inside of another function
def fun1():#wrapper function
    msg = "This is the outer function"

    def fun2():
        print(msg)

    fun2()

fun1()
# 4. What is the scope of a variable in a function WITH an inner function?
    #local INCLUDING the inner function

# 5. Why do we use inner functions?
    #a. access to local variables without needing to pass information in parameters
    #b. to organizes sections of your function


# 6. What is a closure function?
def fun(a):
    #Outer function remembers the value of a

    def adder(b):
        return a+b
    return adder #retrun the closure

val = fun(10)

print(val(5))


# 7. Why do we write closure functions?
    #decrease the num of parameters

def end(income):

    def calc(cost, type):
        percent = cost/income *100
        print(f"Your {type} is ${cost:.2f} and that is {percent:.0f}%")
    return calc

def user_input(type):
    return int(input(f"What is your monthly {type}: \n$"))

income = user_input("Income")
rent = user_input("rent")
utilites = user_input("utilities")
transportation = user_input("transportation")

ready = end(income)

ready(rent, "rent")
ready(utilites, "utilities")
ready(transportation, "transportation")

