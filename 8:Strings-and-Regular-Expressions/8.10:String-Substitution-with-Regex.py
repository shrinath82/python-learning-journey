#`re.sub()` replaces text matching a pattern.
#Example 1 – Remove Numbers
import re
text = "Enemy123"
result = re.sub(r"\d+", "", text)
print(result)

#Output: Enemy


#Example 2 – Replace Numbers
import re
text = "Enemy123"
result = re.sub(r"\d+", "BOSS", text)
print(result)

#Output: EnemyBOSS


#Example 3 – Remove Extra Spaces
import re
text = "Dragon    Goblin     Orc"
result = re.sub(r"\s+", " ", text)
print(result)

#Output: Dragon Goblin Orc