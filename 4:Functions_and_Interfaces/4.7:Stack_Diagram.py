#Understand how functions call one another.
#Example
def weapon():
    print("Sword")

def player():
    weapon()

player()

#Output: Sword

#Another Example
def score():
    print("Score Updated")

def game():
    score()

game()


#Output: Score Updated