"""
Lists are the first major Python collection type in this learning path. They allow you to keep many related values together and modify that collection as the program runs.

A list is an ordered collection of values.

Sword   Bow   Dagger
  0      1      2
"""

#Example 1 – Access List Elements
animals = ["Dragon", "Goblin", "Wolf"]
print(animals[0])
print(animals[2])

#Output: Dragon Wolf


#Example 2 – Print the Whole List
levels = [1, 2, 3, 4, 5]
print(levels)

#Output: [1, 2, 3, 4, 5]


#Example 3 – Negative Index
weapons = ["Sword", "Bow", "Dagger"]
print(weapons[-1])
print(weapons[-2])

#Output: Dagger Bow


#Example 4 – List with Different Types
# A Python list can contain values of different types.
player = ["Krishna", 100, True]
print(player)

#Output: ['Krishna', 100, True]