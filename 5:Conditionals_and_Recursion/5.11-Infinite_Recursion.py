#5.11 Infinite Recursion
#Example
def hello():
    hello()

hello()

#RecursionError: maximum recursion depth exceeded