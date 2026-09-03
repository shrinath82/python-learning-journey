#Markov = predict next word from previous. Simplest version is random choice from possibilities.
#Exercise 8: Random NPC messages - Your Exercise 3
"""
Question: Generate random NPC messages like `Goblin attacks`
Steps:
- Import random
- Create subjects list
- Create verbs list
- Print `random.choice(subjects) + random.choice(verbs)`
"""


#Example 1: Your Exercise 3 - NPC Messages
import random
subjects = ["Goblin", "Dragon", "Wizard"]
verbs = ["attacks", "sleeps", "flies"]
print(random.choice(subjects), random.choice(verbs))
#Output:
# Dragon sleeps (random)

#Example 2: Simple Markov choice
import random
next_words = {
    "dragon": ["attacks", "sleeps", "flies"],
    "goblin": ["hides", "runs", "attacks"]
}
current = "dragon"
print(random.choice(next_words[current]))
#Output:
# attacks (random from 3)

#Example 3: Full game world representation from notes
enemy = {
    "name": "Dragon",
    "health": 500,
    "position": (100, 200),
    "loot": ["Gold", "Sword"]
}
print(enemy)
print(enemy["position"][0])
#Output:
# {'name': 'Dragon', 'health': 500, 'position': (100, 200), 'loot': ['Gold', 'Sword']}
# 100

#Example 4: Quest generator
import random
subjects = ["Dragon", "Goblin", "Wizard"]
verbs = ["attacks", "guards", "finds"]
objects = ["treasure", "village", "sword"]
print(f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}")
#Output:
# Goblin guards sword (random)

"""
Debugging tips for this chapter:
- Always `import random` before using it
- Check `random.choice([])` -Error if empty list, handle with if
- Initialize `counts = {}` before counting loop
"""