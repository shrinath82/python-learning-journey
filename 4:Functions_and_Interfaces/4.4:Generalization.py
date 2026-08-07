# Use parameters so one function works for many situations.
#Example
"""
import turtle

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

square(50)
turtle.done()


#Output: A square with sides of 50 pixels.
"""

#Another Example
import turtle

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

square(150)
turtle.done()

#Output: A larger square.