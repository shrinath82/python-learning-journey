#A file can be processed one line at a time.
#Create a file called `monsters.txt`:
#Dragon
#Goblin
#Orc
#Then run:
with open("monsters.txt") as file:
    for line in file:
        print(line.strip())

#Output
#Dragon
#Goblin
#Orc

#`strip()` removes the newline character at the end of each line.

#Example 2 – Number of Lines
#Using the same `monsters.txt`:
count = 0
with open("monsters.txt") as file:
    for line in file:
        count += 1

print("Monsters:", count)

#Output: Monsters: 3