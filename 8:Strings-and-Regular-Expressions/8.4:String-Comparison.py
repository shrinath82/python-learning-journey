#Strings can be compared using comparison operators.
#Example 1 – Equal
print("apple" == "apple")

#Output: True

#Example 2 – Not Equal
print("apple" != "orange")

#Output: True

#Example 3 – Alphabetical Comparison
print("apple" < "banana")

#Output: True

#Example 4 – Greater Than
print("zebra" > "apple")

#Output: True
#compares strings based on their character values.

#Example 5 – Game Command
command = "start"
if command == "start":
    print("Starting Game")

#Output: Starting Game

#Example 6 – Multiple Commands
command = "attack"
if command == "start":
    print("Starting Game")
elif command == "attack":
    print("Attacking Enemy")
elif command == "quit":
    print("Leaving Game")
else:
    print("Unknown Command")

#Output: Attacking Enemy