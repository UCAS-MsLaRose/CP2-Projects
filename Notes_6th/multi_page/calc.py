# Vienna LaRose, Basics calcualtions funcitons 
num = 10

def get_num():
    return int(input("Tell me a number:\n"))

def addition():
    return get_num()+get_num()

def subtraction(x, y):
    return x-y

def division(x, y):
    return x/y

def multiplication(x, y):
    return x*y


if __name__ == "main":
    multiplication(5,2)