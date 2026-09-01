#For game data that should not change like coordinates, colors.
"""
Exercise 1: Create and access tuple
Question: Create `player_position = (250, 400)` and print x and y separately.
Steps:
- Create tuple with (250, 400)
- Access index 0 for x
- Access index 1 for y
- Print both
"""

# 11.1: Tuples are ordered sequences like lists but immutable. Used for (x,y), RGB, screen size.
player_position = (250, 400)
print(player_position[0])
print(player_position[1])
#Output:
# 250
# 400



#Example 2: RGB color
color = (255, 0, 0)
print(color)
#Output:
# (255, 0, 0)

# Example 3: Access in game context
player = ("Hero", 100)
print(player[0])
print(player[1])
#Output:
# Hero
# 100