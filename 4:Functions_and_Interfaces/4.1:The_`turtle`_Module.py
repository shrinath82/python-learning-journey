#4.1:The_`turtle`_Module
#A module is a collection of reusable  code.
#Example 1 – Import a Module
import turtle
print("Turtle module imported successfully.")

#Output: Turtle module imported successfully.


#Example 2 – Draw a Line
import turtle
t = turtle.Turtle()
t.forward(100)
turtle.done()

#Output: A graphics window opens and the turtle draws a straight line.


#Example 3 – Change Direction
import turtle
t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(50)

turtle.done()

#Output: The turtle draws an L-shaped path.