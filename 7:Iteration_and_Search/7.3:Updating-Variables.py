#Variables can change during every iteration of a loop.
#Example 1 – Increase
count = 0
for i in range(5):
    count = count + 1

print(count)

#Output: 5

"""
#Example 2 – Decrease
count = 10
for i in range(3):
    count = count - 1

print(count)

#Output: 7
"""

"""
#Example 3 – Add Another Value
count = 10
for i in range(3):
    count = count + 5

print(count)

#Output: 25
"""

"""
#Example 4 – Multiply
count = 3
for i in range(3):
    count = count * 2

print(count)

#Output: 24
"""

"""
#Example 5 – Divide
count = 100

for i in range(2):
    count = count / 2

print(count)

#Output: 25.0
"""

#Example 6 – Floor Division
count = 100

for i in range(3):
    count = count // 3

print(count)

#Output: 3

#Example 7 – Modulus
count = 10

for i in range(3):
    count = count % 3

print(count)

#Output: 1


#Example 8 – Power
count = 2

for i in range(3):
    count = count ** 2

print(count)

#Output: 256
#The values are: 2 → 4 → 16 → 256


#Example 9 – Replace Completely
count = 10

for i in range(3):
    count = 100

print(count)

#Output: 100
#Notice that this does not accumulate. The variable is simply assigned `100` each time.