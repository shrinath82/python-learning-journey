#Dictionary Subtraction - actually Set Subtraction. For save games, inventory diff.
#Exercise 5: Compare inventories
"""
Question: Find what is in inventory1 but not in inventory2.
Steps:
- Create two sets
- Use `-` operator
- Print result
"""


#Example 1
inventory1 = {"Sword", "Potion"}
inventory2 = {"Sword"}
print(inventory1 - inventory2)
#Output:
# {'Potion'}

#Example 2
a = {"Sword", "Potion"}
b = {"Potion"}
print(a - b)
#Output:
# {'Sword'}

#Example 3: Level changes / loot diff
old_save = {"Gold", "Shield"}
new_save = {"Gold", "Shield", "Sword", "Potion"}
print(new_save - old_save)
#Output:
# {'Sword', 'Potion'}