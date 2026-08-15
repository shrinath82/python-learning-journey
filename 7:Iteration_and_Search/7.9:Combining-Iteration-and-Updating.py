#This is a very common game-programming pattern.
#Example 1 – Score
score = 0
for i in range(5):
    score += 10

print(score)

#Output: 50

#Example 2 – Health
health = 100
for i in range(3):
    health -= 10

print(health)

#Output: 70

#Example 3 – Multiple Players
players = ["Alice", "Bob", "Charlie"]

for player in players:
    print("Player:", player)

#Output
#Player: Alice
#Player: Bob
#Player: Charlie