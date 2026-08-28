# 10.6 Lists and Dictionaries
# - How games store all_players, all_enemies

players = [
    {"name": "Hero", "health": 100},
    {"name": "Mage", "health": 80}
]


# Example 1: Access first player name
print(players[0]["name"])
# Output: Hero


# Example 2: Loop through all entities
enemies = [
    {"name": "Goblin", "health": 30},
    {"name": "Dragon", "health": 500}
]
for enemy in enemies:
    print(enemy["name"], "has", enemy["health"], "HP")
# Output:
# Goblin has 30 HP
# Dragon has 500 HP