#Functions that return `True` or `False`.
#Example 1
def is_adult(age):
    return age >= 18

print(is_adult(20))

#Example 2
def can_enter(level):
    return level >= 5

print(can_enter(3))
print(can_enter(10))

#Example 3
def has_health(health):
    return health > 0

print(has_health(0))