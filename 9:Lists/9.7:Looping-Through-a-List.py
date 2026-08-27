#This is one of the most important patterns in game programming.

#Example 1 – Inventory
inventory = ["Sword", "Shield", "Potion"]
for item in inventory:
    print(item)

#Output:
#Sword
#Shield
#Potion


#Example 2 – Enemies
enemies = ["Dragon", "Goblin", "Orc"]
for enemy in enemies:
    print("Enemy:", enemy)

#Output: 
#Enemy: Dragon
#Enemy: Goblin
#Enemy: Orc


#Example 3 – List + Conditional
enemies = ["Dragon", "Goblin", "Orc"]
for enemy in enemies:
    if enemy == "Dragon":
        print("Boss found")


#Output: Boss found


#Example 4 – Modify Values During Iteration
scores = [100, 200, 300]
for score in scores:
    print(score + 50)

"""
Output
150
250
350
This prints modified values but does not modify the original list.
"""