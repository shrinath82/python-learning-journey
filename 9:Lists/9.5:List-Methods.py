#Example 1 – `append()`
#Adds one item to the end.
inventory = []
inventory.append("Sword")
inventory.append("Shield")
print(inventory)

#Output: ['Sword', 'Shield']


#Example 2 – `remove()`
#Removes a specific item.
inventory = ["Sword", "Shield", "Potion"]
inventory.remove("Shield")
print(inventory)

#Output: ['Sword', 'Potion']

#Example 3 – `pop()`
#Removes and returns the last item.
inventory = ["Sword", "Shield", "Potion"]
item = inventory.pop()
print("Removed:", item)
print("Inventory:", inventory)

#Output:
#Removed: Potion
#Inventory: ['Sword', 'Shield']


#Example 4 – `pop()` with an Index
inventory = ["Sword", "Shield", "Potion"]
item = inventory.pop(1)
print("Removed:", item)
print("Inventory:", inventory)

#Output
#Removed: Shield
#Inventory: ['Sword', 'Potion']


#Example 5 – `insert()`
#Although not explicitly listed in the notes, it is a common list operation.
inventory = ["Sword", "Potion"]
inventory.insert(1, "Shield")
print(inventory)

#Output:['Sword', 'Shield', 'Potion']


#Example 6 – `clear()`
# Remove all elements.
inventory = ["Sword", "Shield", "Potion"]
inventory.clear()
print(inventory)

#Output: []