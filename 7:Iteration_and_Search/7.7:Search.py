#Searching means examining values until you find what you want.
#Example 1 – Search a List
numbers = [10, 20, 30]
for n in numbers:
    if n == 20:
        print("Found")

#Output: Found

#Example 2 – Search for an Item
items = ["sword", "shield", "potion"]
for item in items:
    if item == "potion":
        print("Found Potion")

#Output: Found Potion

#Example 3 – Search and Stop, Once something is found, `break` can stop the loop.
items = ["sword", "shield", "potion", "key"]
for item in items:
    if item == "potion":
        print("Found Potion")
        break

#Output: Found Potion

#Example 4 – Search for a Character
name = "Krishna"
if "a" in name.lower():
    print("Contains a")

#Output: Contains a

#Example 5 – Search for a Number
numbers = [5, 12, 18, 25, 30]
for number in numbers:
    if number > 20:
        print("Found:", number)

#Output
#Found: 25
#Found: 30
#Here the search finds all numbers greater than 20.