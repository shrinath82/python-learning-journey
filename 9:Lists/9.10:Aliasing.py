# Two variables can refer to the same list object.

#Example 1 – Basic Aliasing
a = [1, 2]
b = a
b.append(3)

print(a)
print(b)

"""
Output
[1, 2, 3]
[1, 2, 3]
Changing `b` also changed `a`.
"""


#Example 2 – Game Inventory
inventory = ["Sword"]
backup = inventory
backup.append("Potion")
print("Inventory:", inventory)
print("Backup:", backup)

"""
Output
Inventory: ['Sword', 'Potion']
Backup: ['Sword', 'Potion']

Both variables refer to the same list.
"""