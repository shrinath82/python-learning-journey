#Exercise 1
def square(size):

Call it with:
50
100
150

Expected Result: Three squares of different sizes.



#Exercise 2
def polygon(sides, length):


Call it to draw:
Triangle
Square
Pentagon

Solution: 
import turtle

def polygon(sides, length):
    angle = 360 / sides

    for i in range(sides):
        turtle.forward(length)
        turtle.left(angle)

polygon(3, 80)
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

polygon(4, 80)
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()

polygon(5, 80)

turtle.done()


#Exercise 3
def reward(points):
    print("Reward:", points)

Call it with:
100
500
1000

Expected Output:
Reward: 100
Reward: 500
Reward: 1000