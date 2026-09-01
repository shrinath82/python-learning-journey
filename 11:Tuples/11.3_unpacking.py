#Tuple unpacking breaks tuple into variables. Very useful for positions.
#Exercise 3: Unpack location
"""
Question: Unpack `location = (50, 75)` into x,y and print.
Steps:
- Create tuple
- Unpack using `x, y = location`
- Print x and y
"""

# Example 1
location = (50, 75)
x, y = location
print(x)
print(y)
#Output:
# 50
# 75

# Example 2: Game movement
player_position = (300, 400)
x, y = player_position
x = x + 10 # move right
print(x, y)
#Output:
# 310 400

# Example 3: Unpacking with 3 values (RGB)
color = (0, 255, 0)
r, g, b = color
print(r)
print(g)
print(b)
#Output:
# 0
# 255
# 0