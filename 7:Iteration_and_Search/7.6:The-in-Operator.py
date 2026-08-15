#The `in` operator checks whether a value exists inside another object.
#Example 1 – Character in String
print("a" in "dragon")

#Output: True

#Example 2 – Character Not Present
print("z" in "dragon")

#Output: False

#Example 3 – String Inside String
print("drag" in "dragon")

#Output: True

#Example 4 – Item in List
inventory = ["sword", "shield", "key"]
print("key" in inventory)

#Output: True

#Example 5 – Item Not in List
inventory = ["sword", "shield", "key"]
print("potion" in inventory)

#Output: False

#Example 6 – Using `in` in a Condition
inventory = ["sword", "shield", "key"]
if "key" in inventory:
    print("Door can be opened")

#Output: Door can be opened