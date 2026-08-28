# 10.9 Debugging - Common Mistakes

player = {"health": 100, "score": 0}


# Example 1: Fix Missing Key with 'in'
if "mana" in player:
    print(player["mana"])
else:
    print("mana key missing - safe handled")
# Output: mana key missing - safe handled


# Example 2: Wrong case vs correct case
print(player["health"])
# Output: 100
# print(player["Health"]) would give Output: KeyError: 'Health'


# Example 3: Safe loop deletion using list()
for key in list(player.keys()):
    if key == "score":
        del player[key]
print(player)
# Output: {'health': 100}