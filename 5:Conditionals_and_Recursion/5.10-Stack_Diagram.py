#5.10 Stack Diagram (Recursion)
def countdown(n):
    print(n)

    if n > 0:
        countdown(n - 1)

countdown(3)