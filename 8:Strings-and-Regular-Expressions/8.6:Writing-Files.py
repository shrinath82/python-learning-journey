#Programs can save information to disk.

#Example 1 – Save a Score
with open("score.txt", "w") as file:
    file.write("500")
print("Score saved")

#Output: Score saved
#The file `score.txt` now contains: 500



#Example 2 – Save Player Name
with open("player.txt", "w") as file:
    file.write("Hero")
print("Player saved")

#Output: Player saved



#Example 3 – Save Multiple Values
with open("savegame.txt", "w") as file:
    file.write("Level=5\n")
    file.write("Score=1200\n")

print("Game saved")

"""
Output: Game saved
The resulting file:
Level=5
Score=1200
"""


#Example 4 – Write User Input
name = input("Player name: ")
with open("player.txt", "w") as file:
    file.write(name)

print("Player saved")

"""
Sample Input: Krishna
Output: 
Player name: Krishna
Player saved
"""