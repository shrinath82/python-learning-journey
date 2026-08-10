#Recursive functions can also return values.
#Example 1 – Factorial
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

#Example 2 – Sum of Numbers
def total(n):
    if n == 1:
        return 1

    return n + total(n - 1)

print(total(5))