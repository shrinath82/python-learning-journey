#Example 1 – Ascending Order
scores = [400, 100, 900, 200]
scores.sort()
print(scores)

#Output: [100, 200, 400, 900]


#Example 2 – Descending Order
scores = [400, 100, 900, 200]
scores.sort(reverse=True)
print(scores)


#Output: [900, 400, 200, 100]


#Example 3 – Alphabetical Sorting
weapons = ["Sword", "Bow", "Dagger", "Axe"]
weapons.sort()
print(weapons)


#Output: ['Axe', 'Bow', 'Dagger', 'Sword']


#Example 4 – `sorted()`
#`sorted()` creates a new sorted list without modifying the original.
scores = [400, 100, 900, 200]
sorted_scores = sorted(scores)
print("Original:", scores)
print("Sorted:", sorted_scores)

"""
Output: 
Original: [400, 100, 900, 200]
Sorted: [100, 200, 400, 900]
"""