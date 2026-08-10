#5.9 Recursion
#A function calls itself.
#Example 1 – Countdown
def countdown(n):
    print(n)

    if n > 0:
        countdown(n - 1)

countdown(5)

#Example 2 – Count Up
def count_up(n):
    if n > 5:
        return

    print(n)

    count_up(n + 1)

count_up(1)