#Example 1 – NameError
print(total)
#correct: print("total")

#Example 2 – SyntaxError
age =
print(age)

#Example 3 – IndentationError
if True:
print("Hello")

#Example 4 – TypeError
age = "25"
print(age + 5)


#Correct version:
#age = int("25")
#print(age + 5)

#Example 5 – ModuleNotFoundError
import abcxyz