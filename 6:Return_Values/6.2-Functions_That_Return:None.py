# 6.2-Functions_That_Return:None
# If a function doesn't explicitly return a value,  returns `None`.
#Example 1
def hello():
    print("Hi")

result = hello()
print(result)

#Example 2 – Explicit `return`
def greet():
    print("Welcome")
    return

result = greet()

print(result)