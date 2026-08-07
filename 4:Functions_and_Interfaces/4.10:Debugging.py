#Graphics programs often require checking variable values.RUN EVERYTHIN SEPARATELY
#Example 1 – Debug with `print()`
def move(distance):
    print("Distance =", distance)

move(50)
move(100)


Output: 
Distance = 50
Distance = 100


#Example 2 – Invalid Parameter
def move(distance):
    print(distance + 10)

move("Fifty")

Output: TypeError


#Example 3 – Missing Import
t = turtle.Turtle()

Output: NameError: name 'turtle' is not defined


#Example 4 – Coordinate Debugging
x = 120
y = 80
print("Player Position:", x, y)

#Output: Player Position: 120 80