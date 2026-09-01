#Functions return multiple values as a tuple automatically.
#Exercise 4: Multiple return values
"""
Question: Write a function that returns player x,y and unpack it.
Steps:
- Define `get_position()` returning `100, 200`
- Call it as `x, y = get_position()`
- Print x,y
"""

#Example 1
def get_position():
    return 100, 200

x, y = get_position()
print(x)
print(y)
#Output:
# 100
# 200

#Example 2
def player_stats():
    return 100, 50 # health, mana

health, mana = player_stats()
print(health, mana)
#Output:
# 100 50