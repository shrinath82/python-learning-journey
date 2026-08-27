#Lists and strings can be converted between one another.

#Example 1 – `split()`
text = "Sword Shield Potion"
items = text.split()
print(items)


#Output: ['Sword', 'Shield', 'Potion']


#Example 2 – `split()` with a Separator
text = "Sword,Shield,Potion"
items = text.split(",")
print(items)


#Output: ['Sword', 'Shield', 'Potion']


#Example 3 – `join()`
items = ["Sword", "Shield"]
print(",".join(items))

#Output: Sword,Shield


#Example 4 – `join()` with Spaces
items = ["Sword", "Shield", "Potion"]
print(" ".join(items))

#Output: Sword Shield Potion


#Example 5 – Game Command Parsing
command = "attack goblin"
parts = command.split()
print(parts)

#Output: ['attack', 'goblin']


#You can then access individual pieces:
command = "attack goblin"
parts = command.split()
print("Action:", parts[0])
print("Target:", parts[1])

#Output:
#Action: attack
#Target: goblin