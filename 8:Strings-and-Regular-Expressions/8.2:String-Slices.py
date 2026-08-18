"""
Syntax: string[start:end]
The `end` position is not included.
"""

#Example 1 – Basic Slice
word = "dragon"
print(word[0:3])

#Output: dra

#Example 2 – Beginning to Position
word = "adventure"
print(word[0:4])

#Output: adve

#Example 3 – From Position to End
print("GameOver"[4:])

#Output: Over

#Example 4 – From Beginning to Position
word = ""
print(word[:3])

#Output: Pyt

#Example 5 – Negative Slice
word = "dragon"
print(word[-3:])

#Output: gon

#Example 6 – Slice with Step
word = "abcdef"
print(word[0:6:2])

#Output: ace

#Example 7 – Reverse a String
word = "dragon"
print(word[::-1])

#Output: nogard