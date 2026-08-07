#Place repeated logic into a function.
#Example
import turtle

def square():
    for i in range(4):
        turtle.forward(80)
        turtle.left(90)

square()

turtle.done()


#Output: A square is drawn.