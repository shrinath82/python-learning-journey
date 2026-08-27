#Lists can be passed to functions.

#Example 1 – Display a List
def show(items):
    print(items)

inventory = ["Sword", "Potion"]

show(inventory)


#Output: ['Sword', 'Potion']


#Example 2 – Process Every Item
def show_inventory(items):
    for item in items:
        print("Item:", item)

inventory = ["Sword", "Potion", "Key"]

show_inventory(inventory)

"""
Output
Item: Sword
Item: Potion
Item: Key
"""


#Example 3 – Modify a List Through a Function
def add_item(items):
    items.append("Potion")

inventory = ["Sword"]
add_item(inventory)
print(inventory)


#Output: ['Sword', 'Potion']
# This is important: because lists are mutable, a function can modify the list passed to it.