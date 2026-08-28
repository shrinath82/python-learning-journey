# 10.3 The in Operator
# - Checks if KEY exists. Prevents crash.

player = {
    "health": 100,
    "score": 1000
}


# Example 1: Key exists
print("health" in player)
# Output: True


# Example 2: Key does NOT exist
print("mana" in player)
# Output: False


# Example 3: Safe access pattern
if "ammo" in player:
    print(player["ammo"])
else:
    print("No ammo key found")
# Output: No ammo key found