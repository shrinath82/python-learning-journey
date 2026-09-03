#Unique words using set(). Used for keyword extraction, chat analysis.
#Exercise 1: Find unique words
"""
Question: Find unique words from `sentence = "red blue red green"`
Steps:
- Create string
- Use `.split()` to get words
- Wrap with `set()`
- Print
"""

#Example 1
sentence = "red blue red green"
print(set(sentence.split()))
#Output:
# {'red', 'blue', 'green'}

#Example 2
text = "dragon dragon sword"
words = text.split()
print(set(words))
#Output:
# {'dragon', 'sword'}

#Example 3: Count unique
text = "goblin goblin dragon orc"
unique = set(text.split())
print(len(unique))
print(unique)
#Output:
# 3
# {'goblin', 'dragon', 'orc'}