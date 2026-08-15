#This combines several concepts from previous chapters.
#Example – Find a Defeated Enemy
enemies = {
    "Dragon": 0,
    "Goblin": 50,
    "Orc": 0
}

for enemy in enemies:
    if enemies[enemy] <= 0:
        print(enemy, "defeated")

"""
Output
Dragon defeated
Orc defeated
This pattern is much closer to actual game logic.
"""