#3.2-What_Can_Go_Inside_a_Function?
#Anything that is valid Python code.
#A. Print Statement <<<---

def hello():
    print("Hello World")

hello()

#B. Variable Assignment <<<---
def score():
    points = 100
    print(points)

score()

#C. Arithmetic Operations  <<<---
def add():
    a = 20
    b = 30
    total = a + b
    print(total)

add()

#D. Conditional Statement  <<<---
def check_score():
    score = 80

    if score >= 50:
        print("Level Cleared")

check_score()

#E. Loop  <<<---
def countdown():
    for i in range(5, 0, -1):
        print(i)

countdown()

#F. Calling Another Function  <<<---
def welcome():
    print("Welcome")

def start():
    welcome()

start()

#G. Returning a Value   <<<---
def add():
    return 25 + 15

result = add()

print(result)

#H. Reading User Input   <<<---
def player():
    name = input("Enter name: ")
    print("Hello", name)

player()

#Sample Input
#Krishna

#I. Working with Strings  <<<---
def convert():
    name = "python"
    print(name.upper())

convert()

#J. Working with Lists   <<<---
def numbers():
    values = [10, 20]
    values.append(30)
    print(values)

numbers()

#K. Working with Dictionaries  <<<---
def student():
    data = {"name": "John"}
    data["age"] = 20
    print(data)

student()

#L. File Operations  <<<---
def create_file():
    file = open("demo.txt", "w")
    file.write("Python")
    file.close()

    print("File Created")

create_file()

#M. Exception Handling  <<<---
def divide():
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Cannot divide by zero")

divide()

#N. Import Module  <<<---
def calculate():
    import math
    print(math.sqrt(49))

calculate()

#O. Nested Function  <<<---
def outer():

    def inner():
        print("Inner Function")

    inner()

outer()

#P. Define a Class   <<<---
def demo():

    class Player:

        def show(self):
            print("Player Created")

    p = Player()
    p.show()

demo()