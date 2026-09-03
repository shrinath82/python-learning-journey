#Random numbers critical for loot drops, spawns, crits, procedural content.
#Exercise 6: Random loot generator - Your Exercise 1
"""
Question: Create random loot generator from Gold, Potion, Sword, Shield.
Steps:
- Import random
- Create loot list
- Use `random.choice(loot)` and print
"""


#Example 1: Loot generator - Your Exercise 1
import random
loot = ["Gold", "Potion", "Sword", "Shield"]
print(random.choice(loot))
#Output:
# Sword (random - can be any of 4)

#Example 2: Dice roll
import random
print(random.randint(1, 6))
#Output:
# 4 (random 1-6)

#Example 3: Random enemy spawn
import random
enemies = ["Goblin", "Dragon", "Orc"]
print(random.choice(enemies))
#Output:
# Dragon (random)

#Example 4: Multiple random choices
import random
loot = ["Gold", "Potion", "Sword", "Shield"]
for i in range(3):
    print(random.choice(loot))
#Output:
# Gold
# Potion
# Shield (random 3 picks)