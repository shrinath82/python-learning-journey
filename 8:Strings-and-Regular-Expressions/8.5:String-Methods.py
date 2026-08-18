#String methods are functions belonging to string objects.
#Example 1 – `upper()`
name = "Krishna"
print(name.upper())

#Output: KRISHNA

"""
#Example 2 – `lower()`
name = "Krishna"
print(name.lower())
#Output: krishna
"""

"""
#Example 3 – `strip()`
Removes whitespace from the beginning and end.
text = "   hello   "
print(text.strip())
#Output: hello
"""

"""
#Example 4 – `replace()`
text = "Goblin Goblin Goblin"
print(text.replace("Goblin", "Dragon"))

#Output: Dragon Dragon Dragon
"""
"""
#Example 5 – `split()`
text = "sword shield potion"
items = text.split()
print(items)

#Output: ['sword', 'shield', 'potion']
"""

"""
#Example 6 – Split Using a Separator
data = "Dragon,Goblin,Orc"
monsters = data.split(",")
print(monsters)

#Output: ['Dragon', 'Goblin', 'Orc']
"""

"""
#Example 7 – `join()`
#The reverse operation of `split()`.
items = ["sword", "shield", "potion"]
result = ", ".join(items)
print(result)

#Output: sword, shield, potion
"""

"""
#Example 8 – `startswith()`
command = "attack dragon"
print(command.startswith("attack"))

#Output: True
"""

"""
#Example 9 – `endswith()`
filename = "savegame.txt"
print(filename.endswith(".txt"))

#Output: True
"""

"""
#Example 10 – `find()`
text = "Dragon Attack"
print(text.find("Attack"))

#Output: 7

#If the text isn't found, `find()` returns `-1`.
text = "Dragon Attack"
print(text.find("Potion"))

#Output: -1
"""