#When writing recursion, assume the smaller recursive call works correctly.
#Example
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(4))

"""
Focus on:
return n * factorial(n - 1)
Assume `factorial(n - 1)` already works.
"""