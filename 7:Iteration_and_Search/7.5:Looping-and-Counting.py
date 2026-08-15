# `range()` is commonly used to control how many times a loop executes.
#Example 1 – `range(10)`


for i in range(10):
    print(i)

"""
Output
0
1
2
3
4
5
6
7
8
9
Important: `range(10)` starts at `0` and stops before 10.
"""

#Example 2 – Count 1 to 10
for i in range(1, 11):
    print(i)

"""
Output
1
2
3
4
5
6
7
8
9
10
"""

#Example 3 – Game Levels
for level in range(1, 6):
    print("Level", level)

"""
Output
Level 1
Level 2
Level 3
Level 4
Level 5
"""

#Example 4 – Countdown
for i in range(5, 0, -1):
    print(i)
"""
Output
5
4
3
2
1
"""
#Example 5 – Step Value
#The third argument controls the step.
for i in range(0, 11, 2):
    print(i)

"""
Output
0
2
4
6
8
10
"""

#Example 6 – Negative Step
for i in range(10, 0, -2):
    print(i)
"""
Output
10
8
6
4
2
"""