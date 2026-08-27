#Example 1 – `IndexError`
#IndexError → Check that the index exists
"""
items = ["Sword"]
print(items[10])

#Output:
#IndexError: list index out of range
#The list has only index `0`.
"""


"""
#Fix IndexError
#The problem is that index 10 doesn't exist.
items = ["Sword"]

if len(items) > 10:
    print(items[10])
else:
    print("Index does not exist")

#Output: Index does not exist
"""      

"""
#OR, if you actually want to access the first item:
items = ["Sword"]
print(items[0])

#Output: Sword
"""


"""
#Example 2 – Removing a Missing Item
#ValueError → Check that the item exists
items = ["Sword", "Shield"]
items.remove("Bow")

#Output: ValueError: list.remove(x): x not in list
"""


"""
#Fix ValueError
#The problem is that "Bow" isn't in the list.
items = ["Sword", "Shield"]

if "Bow" in items:
    items.remove("Bow")
    print(items)
else:
    print("Bow not found")

#Output: Bow not found        
"""

"""
#OR, If you actually want to remove an existing item:
items = ["Sword", "Shield"]

if "Shield" in items:
    items.remove("Shield")

print(items)

#Output: ['Sword']
"""


#Example 3 – Aliasing Bug
#Aliasing → Use .copy() when you need an independent list
inventory = ["Sword"]
backup = inventory
backup.append("Potion")
print(inventory)

"""
Output: ['Sword', 'Potion']

If you expected `inventory` to remain unchanged, this is an aliasing problem.

Use: 
backup = inventory.copy()

instead.
"""

"""
#If you want backup to be an independent copy:
inventory = ["Sword"]
backup = inventory.copy()
backup.append("Potion")
print("Inventory:", inventory)
print("Backup:", backup)

#Output:
#Inventory: ['Sword']
#Backup: ['Sword', 'Potion']
"""
