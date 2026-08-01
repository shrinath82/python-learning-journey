# Import lets us use modules.
#Example 1 – Import math
import math
print(math.sqrt(25))

#Example 2 – Import Random
import random
print(random.randint(1, 10))

#Example 3 – Import Specific Function
from math import pi
print(pi)

#Example 4 – Module Alias
#The factorial of 5 (written as 5!) is calculated by multiplying all whole numbers from 5 down to 1:
#5! = 5 * 4 * 3 * 2 * 1 = 120
import math as m
print(m.factorial(5))