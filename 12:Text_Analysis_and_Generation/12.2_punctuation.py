#Punctuation makes "dragon" and "dragon!" different. Clean before analysis.
#Exercise 2: Clean punctuation
"""
Question: Clean `Dragon, Goblin!` to remove `,` and `!`
Steps:
- Create text
- Replace "," with ""
- Replace "!" with ""
- Print cleaned text
"""

#Example 1
text = "Dragon, Goblin!"
text = text.replace(",", "")
text = text.replace("!", "")
print(text)
#Output:
# Dragon Goblin

#Example 2: More robust cleaning + lowercasing
text = "Dragon! Dragon, dragon."
text = text.lower()
text = text.replace(",", "").replace(".", "").replace("!", "")
print(text)
print(text.split())
#Output:
# dragon dragon dragon
# ['dragon', 'dragon', 'dragon']

#Example 3: Chain replace
text = "Hello, World! How are you?"
cleaned = text.replace(",", "").replace("!", "").replace("?", "")
print(cleaned)
#Output:
# Hello World How are you