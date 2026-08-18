#Regular expressions allow you to search for patterns, rather than only exact text.
#'s regular-expression module is `re`.

#Example 1 – Find Numbers
import re
text = "Player123"
result = re.search(r"\d+", text)
print(result)

"""
Output will look similar to
<re.Match object; span=(6, 9), match='123'>
The important part is that the pattern found:
123
"""


#Example 2 – Check Whether a Number Exists
import re
text = "Dragon99"
if re.search(r"\d+", text):
    print("Contains Number")

"""
Output
Contains Number
"""

#Example 3 – No Number
import re
text = "Dragon"

if re.search(r"\d+", text):
    print("Contains Number")
else:
    print("No Number")

#Output: No Number