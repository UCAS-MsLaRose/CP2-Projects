# Vienna LaRose, Advanced Functions Notes

# 1. What is a helper function?
    #A function written to be called in another function
def is_int(user_input):
    try:
        int(user_input)
    except:
        # 8. What is recursion?
            #when you call a funciton inside of itself
        # 9. How does recursion work?
        print("Please give me a number.")
        user_input = is_int(input("How old are you?\n"))
    return user_input
    
def age():
    old = is_int(input("How old are you?\n"))

    print(f"Cool. You are {old}")

age()

# 2. What is the purpose of a helper function?
    #You have this I am not writing it :)
# 3. What is an inner function?
    #A function that is inside of anther funciton
def add(a):
    b = int(input("Give me a number\n"))

    def addition():
        print(a+b)

    addition()

#add(3)
import logging

logging.basicConfig(level=logging.INFO)

def logger(func):

    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}")
        return func(*args, *kwargs)
    return wrapper

#@logger
def adder(a,b):
    return a+b


#print(adder(3,4))
# 4. What is the scope of a variable in a function WITH an inner function?
    #You have this I am not writing it :)
# 5. Why do we use inner functions?
    #You have this I am not writing it :)
# 6. What is a closure function?
def add(a):

    def addition(b):
        return a+b

    return addition

base = add(10)

#print(base(5))
#EXAMPLE
def math(income):

    def perc(amount, type):
        percent = amount/income*100
        print(f"Your {type} is ${amount}, and that is {percent}% of your income")
    return perc
    
def user_inputs(type):
    return int(input(f"What is your monthly {type}\n$"))

income = user_inputs("income")
rent = user_inputs("rent")
utilities = user_inputs("utilities")
groceries = user_inputs("groceries")
transportation = user_inputs("transportation")

start = math(income)
start(rent, "rent")




# 7. Why do we write closure functions?