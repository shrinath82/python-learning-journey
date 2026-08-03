#3.6-Local_Variables
#Example 1 – Local Variable Works

def demo():
    score = 100
    print(score)

demo()

"""
#Example 2 – Local Variable Outside Function
def demo():
    score = 100

demo()

print(score)
#NameError: name 'score' is not defined - EXPECTED
"""