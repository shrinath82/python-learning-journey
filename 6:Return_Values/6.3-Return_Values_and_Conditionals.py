#6.3-Return_Values_and_Conditionals
#Returned values can be used directly inside `if` statements.
#Example 1 – Boolean Return
def is_even(n):
    return n % 2 == 0

print(is_even(10))

#Example 2 – Using in `if`
def is_even(n):
    return n % 2 == 0

if is_even(8):
    print("Even")

#Example 3 – `False` Case
def is_even(n):
    return n % 2 == 0

if is_even(7):
    print("Even")
else:
    print("Odd")