#`replace()` searches for matching text and creates a new string.
#Example 1
text = "Goblin Goblin Goblin"
result = text.replace("Goblin", "Dragon")
print(result)

#Output: Dragon Dragon Dragon


#Example 2 – Replace Only Once
text = "Goblin Goblin Goblin"
result = text.replace("Goblin", "Dragon", 1)
print(result)

#Output: Dragon Goblin Goblin