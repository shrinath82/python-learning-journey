#3.10-Debugging_Functions
#A. Missing Argument
def greet(name):
    print(name)

greet()

#Output: TypeError: greet() missing 1 required positional argument: 'name'

#B. Wrong Function Name
def hello():
    print("Hello")

helo()

#Output: NameError: name 'helo' is not defined


#C. Wrong Number of Arguments
def add(a, b):
    print(a + b)

add(10)

#Output: TypeError

#D. Scope Problem
def test():
    x = 10

print(x)

#Output: NameError


#E. Return Value Ignored
def add():
    return 10 + 20

add()

print("Finished")

#Output: Finished
#The function returns `30`, but because the return value isn't used or printed, it is discarded.