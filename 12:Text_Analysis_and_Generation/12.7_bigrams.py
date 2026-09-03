#Bigram = pair of consecutive words. Used for predictive text, dialogue.
#Exercise 7: Generate bigrams
"""
Question: Generate bigrams from `the dragon attacks`
Steps:
- Split text to words
- Loop `range(len(words)-1)`
- Print `(words[i], words[i+1])`
"""


#Example 1
words = "the dragon attacks".split()
for i in range(len(words)-1):
    print((words[i], words[i+1]))
#Output:
# ('the', 'dragon')
# ('dragon', 'attacks')

#Example 2: Longer sentence
text = "the dragon guards the treasure"
words = text.split()
bigrams = []
for i in range(len(words)-1):
    bigrams.append((words[i], words[i+1]))
print(bigrams)
#Output:
# [('the', 'dragon'), ('dragon', 'guards'), ('guards', 'the'), ('the', 'treasure')]

#Example 3: Count bigrams
words = "red blue red blue red green".split()
freq = {}
for i in range(len(words)-1):
    pair = (words[i], words[i+1])
    freq[pair] = freq.get(pair, 0) + 1
print(freq)
#Output:
# {('red', 'blue'): 2, ('blue', 'red'): 2, ('red', 'green'): 1}