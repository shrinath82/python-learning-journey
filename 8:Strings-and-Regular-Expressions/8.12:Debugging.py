#Example 1 – `IndexError`
name = ""
print(name[0])

"""
Output
IndexError: string index out of range
The string has no character at index `0`.
"""


"""
##Safe Version
name = ""
if name:
    print(name[0])
else:
    print("Name is empty")

#Output: Name is empty
"""

"""
#Example 2 – `FileNotFoundError`
with open("missing.txt") as file:
    print(file.read())

#Output: FileNotFoundError
"""

"""
##Safer Version
import os
filename = "missing.txt"
if os.path.exists(filename):
    with open(filename) as file:
        print(file.read())
else:
    print("File does not exist")


#Output: File does not exist
"""

"""
#Example 3 – Regex Debugging
Start with a small string:
import re
text = "Player123"
match = re.search(r"\d+", text)

if match:
    print("Found:", match.group())
else:
    print("Nothing found")

#Output: Found: 123
#Testing a small string first makes regex problems much easier to isolate.
"""