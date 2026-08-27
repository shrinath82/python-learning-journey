"""
Create `names.txt`
nano names.txt
Dragon
Goblin
Orc

Note: Make sure you have both the file and the script in the same directory. Also, running the script from inside the folder.
"""

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

print(names)


#Output: ['Dragon', 'Goblin', 'Orc']


#Example 2 – Count the Names
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

print("Number of monsters:", len(names))


#Output: Number of monsters: 3