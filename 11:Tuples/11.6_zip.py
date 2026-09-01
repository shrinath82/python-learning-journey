#zip() combines sequences into list of tuples.
#Exercise 6: Combine lists with zip
"""
Question: Use zip() to combine names and scores.
Steps:
- Create names list
- Create health list
- Zip them and loop print
"""


#Example 1
names = ["Hero", "Mage"]
health = [100, 80]
print(list(zip(names, health)))
#Output:
# [('Hero', 100), ('Mage', 80)]

#Example 2: Your exercise
names = ["Goblin", "Dragon"]
health = [50, 500]
for enemy, hp in zip(names, health):
    print(enemy, hp)
#Output:
# Goblin 50
# Dragon 500
