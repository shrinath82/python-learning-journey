# 10.2 Accessing Values
# - Dict["key"] gives value. KeyError if missing.

player = {
    "name": "Hero",
    "health": 100
}


# Example 1: Access health
print(player["health"])
# Output: 100


# Example 2: Access name
print(player["name"])
# Output: Hero