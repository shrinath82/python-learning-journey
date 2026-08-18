"""
A string stores characters in a specific order, and each character has an index.
d r a g o n
0 1 2 3 4 5
"""
#Example 1 – Access Characters
word = "dragon"
print(word[0])
print(word[3])

"""
Output
d
g
"""

#Example 2 – Last Character
#Negative indexes count from the end.
word = "dragon"

print(word[-1])
print(word[-2])

"""
Output
n
o
"""

#Example 3 – User Input
name = input("Name: ")
print(name[0])


#Sample Input: Krishna

"""
Output
Name: Krishna
K
"""

#Example 4 – Access Every Character
word = "dragon"
for i in range(len(word)):
    print(i, word[i])

"""
Output
0 d
1 r
2 a
3 g
4 o
5 n
"""