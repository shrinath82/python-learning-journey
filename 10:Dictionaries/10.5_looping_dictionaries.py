# 10.5 Looping and Dictionaries

player = {
    "health": 100,
    "mana": 50,
    "score": 1000
}


# Example 1: Loop keys only
for key in player:
    print(key)
# Output:
# health
# mana
# score


# Example 2: Loop keys + values
for key in player:
    print(key, player[key])
# Output:
# health 100
# mana 50
# score 1000


# Example 3: Using.items() - Best practice
for key, value in player.items():
    print(f"{key}: {value}")
# Output:
# health: 100
# mana: 50
# score: 1000