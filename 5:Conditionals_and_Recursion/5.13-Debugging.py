#5.13 Debugging
#A. Wrong Comparison Operator

score = 100
"""
if score = 100:
    print("Winner")

#Output: SyntaxError
#Correct: score = 100
"""
if score == 100:
    print("Winner")

#Output:Winner


#B. Infinite Recursion
def test():
    test()

test()

Output: RecursionError

#C. Input Type Error
age = input("Age: ")
print(age + 5)

#Sample Input: 25
#Output:TypeError

age = int(input("Age: "))
print(age + 5)


#Sample Input: 25
#Output: Age: 25