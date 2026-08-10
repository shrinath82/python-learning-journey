#5.2-Modulus (`%`)
#Returns the remainder after division.
#Example 1
print(17 % 5)

#Example 2 – Every 3rd Level
for level in range(1, 11):
    if level % 3 == 0:
        print("Bonus Level:", level)

#Example 3 – Odd or Even
number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")