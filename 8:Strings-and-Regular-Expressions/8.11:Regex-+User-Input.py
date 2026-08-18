#This is closer to a practical game command.
#Example
import re
command = input("Enter command: ")
if re.search(r"\d+", command):
    print("Command contains a number")
else:
    print("No number found")

"""
Sample Input
attack 5

Output
Enter command: attack 5
Command contains a number
"""