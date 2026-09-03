#Frequency counting using dict.get(). For logs, chat analysis, game stats.
#Exercise 3: Count frequencies - Your Exercise 2
"""
Question: Count word frequencies in `dragon dragon dragon sword sword`
Steps:
- Create text
- Split into words
- Create empty dict `counts = {}`
- Loop words, use `counts.get(word, 0) + 1`
- Print counts
"""

#Example 1: Your Exercise
text = "dragon dragon dragon sword sword"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)
#Output:
# {'dragon': 3, 'sword': 2}

#Example 2: List version
words = ["dragon", "dragon", "sword"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
#Output:
# {'dragon': 2, 'sword': 1}

#Example 3: Find most frequent
text = "goblin orc goblin dragon goblin"
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
print(counts)
print(max(counts, key=counts.get))
#Output:
# {'goblin': 3, 'orc': 1, 'dragon': 1}
# goblin