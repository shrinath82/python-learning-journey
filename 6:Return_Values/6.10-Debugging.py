#A. Forgot `return`
#Wrong:
def add(a, b):
    a + b

print(add(5, 6))

#Output: None

"""
#Correct:

def add(a, b):
    return a + b

print(add(5, 6))
"""

#B. Returning the Wrong Type
#Wrong:

def passed():
    return "True"

print(type(passed()))


#Output: <class 'str'>

"""
#Correct

def passed():
    return True

print(type(passed()))
"""

#C. Recursive Function Without a Base Case

def test(n):
    return test(n + 1)

print(test(1))