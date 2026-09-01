#Exercise 2: Prove immutability
"""
Question: Try to change a tuple and observe error.
Steps:
- Create `position = (100, 200)`
- Print it
- Try to assign `position[0] = 500`
"""

# 11.2:Tuples cannot be modified after creation. Good for SCREEN_SIZE = (1280,720)
# Example 1: Working code
position = (100, 200)
print(position)
#Output:
# (100, 200)

# Example 2: This will fail - comment it before running Example 1
# position = (100, 200)
# position[0] = 500 # TypeError: 'tuple' object does not support item assignment
# print(position)
#Output:
# TypeError: 'tuple' object does not support item assignment

# Example 3: Correct way is to create new tuple
position = (100, 200)
position = (500, 200)
print(position)
#Output:
# (500, 200)