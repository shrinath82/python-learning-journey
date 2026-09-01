#*args packs multiple arguments into a tuple. Useful when count is unknown.
#Exercise 5: Argument packing with *args
"""
Question: Collect unknown number of items into tuple using `*items`.
Steps:
- Define `collect(*items)` and print items
- Call with "Gold", "Potion", "Sword"
"""

#Example 1
def collect(*items):
    print(items)

collect("Gold", "Potion", "Sword")
#Output:
# ('Gold', 'Potion', 'Sword')

#Example 2: Game example
def spawn_enemies(*enemies):
    for e in enemies:
        print(f"Spawning {e}")

spawn_enemies("Goblin", "Orc")
#Output:
# Spawning Goblin
# Spawning Orc