#You cannot directly change an individual character.
#Example 1 – Invalid Modification
"""
name = "dragon"
name[0] = "D"
print(name)
#Output: TypeError: 'str' object does not support item assignment
"""


#Example 2 – Correct Way to Create a Modified String
name = "dragon"
new_name = "D" + name[1:]
print(new_name)
#Output: Dragon



#Example 3 – Another Way
name = "dragon"
name = name.upper()
print(name)
#Output: DRAGON
#The original string isn't modified. A new string is produced and assigned to `name`.