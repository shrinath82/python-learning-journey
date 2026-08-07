#Example 1 – Without a Loop
import turtle
t = turtle.Turtle()

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

turtle.done()
#Output: A square is drawn.


"""
#Example 2 – Using a Loop (Preferred)
import turtle
t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
# Output: A square is drawn using much less code.
"""