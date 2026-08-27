#Exercise 1 – Inventory
#Task: Create and display a player's inventory.
"""
Steps:
* Create `inventory` with `"Sword"` and `"Shield"`.
* Add `"Potion"` using a list method.
* Add `"Key"` using a list method.
* Loop through the list and display every item.

Expected Output:
Sword
Shield
Potion
Key
"""

#Solution: 
inventory = ["Sword", "Shield"]
inventory.append("Potion")
inventory.append("Key")
for item in inventory:
    print(item)




#Exercise 2 – High Scores
#Task: Sort a list of game scores from lowest to highest.
"""
Steps:
* Create `scores = [500, 1200, 800, 200]`.
* Sort the list using a list method.
* Print the sorted list.

Expected Output: [200, 500, 800, 1200]
"""

#Solution:
scores = [500, 1200, 800, 200]
scores.sort()
print(scores)



#Exercise 3 – Monster File
#Task: Read monster names from a file and store them in a list.
"""
Steps:
* Create `monsters.txt`.
* Add `Dragon`, `Goblin`, and `Orc`, each on a separate line.
* Create an empty list called `monsters`.
* Open the file.
* Loop through each line.
* Remove the newline using `.strip()`.
* Add each name to the list.
* Print the list.

Expected Output: ['Dragon', 'Goblin', 'Orc']
"""

#Solution:
monsters = []
with open("monsters.txt") as file:
    for line in file:
        monsters.append(line.strip())

print(monsters)