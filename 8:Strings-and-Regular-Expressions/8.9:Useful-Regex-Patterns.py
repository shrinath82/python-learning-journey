#Understanding a few basic patterns is enough to start.
#Example 1 – `\d` = Digit
import re
text = "Level5"
print(re.search(r"\d", text))

#Output: A match object representing `5`.


#Example 2 – `\d+` = One or More Digits
import re
text = "Level123"
match = re.search(r"\d+", text)
print(match.group())

#Output: 123


#Example 3 – `\w+` = Word Characters
import re
text = "Player_123"
match = re.search(r"\w+", text)
print(match.group())

#Output: Player_123


#Example 4 – `^` = Beginning
import re
text = "Dragon attack"
if re.search(r"^Dragon", text):
    print("Starts with Dragon")

#Output: Starts with Dragon


#Example 5 – `$` = End
import re
text = "Dragon"
if re.search(r"Dragon$", text):
    print("Ends with Dragon")

#Output: Ends with Dragon