#Tuples compare element-wise. Useful for sorting. Dict inversion via tuple swap.
#Exercise 7: Sorting and Inverting
"""
Question: Sort leaderboard and invert dict to (score, name).
Steps:
- Create scores list of tuples
- Use sorted()
- Create dict scores and loop items to print (score, name)
"""


#Example 1: Comparing
print((1, 2) < (1, 3))
#Output:
# True

#Example 2: Sorting by second value automatically? No, sorts by first. So make (score, name) or use key.
scores = [
    ("Alice", 500),
    ("Bob", 800),
    ("Chris", 200)
]
print(sorted(scores))
#Output:
# [('Alice', 500), ('Bob', 800), ('Chris', 200)] - sorted by name

#Example 3: Sort by score
print(sorted(scores, key=lambda x: x[1]))
#Output:
# [('Chris', 200), ('Alice', 500), ('Bob', 800)]

#Example 4: Inverting dictionary for leaderboard
scores_dict = {
    "Alice": 500,
    "Bob": 800
}
for name, score in scores_dict.items():
    print((score, name))
#Output:
# (500, 'Alice')
# (800, 'Bob')

#Example 5: Debugging - common mistake
# Wrong: x = (5) -int
x = (5)
print(type(x))
#Output:
# <class 'int'>

# Correct: x = (5,)
x = (5,)
print(type(x))
print(x)
#Output:
# <class 'tuple'>
# (5,)