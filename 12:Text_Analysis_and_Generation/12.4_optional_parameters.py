#Optional parameters have default values. Makes functions flexible.
#Exercise 4: Optional params
"""
Question: Make a flexible `spawn_enemy` function.
Steps:
- Define `def spawn_enemy(name="Goblin"):`
- Print name inside
- Call with no args and with "Dragon"
"""

#Example 1
def greet(name="Player"):
    print(name)

greet()
greet("Hero")
#Output:
# Player
# Hero

#Example 2
def reward(points=100):
    print(points)

reward()
reward(500)
#Output:
# 100
# 500

#Example 3: Game function
def spawn_enemy(name="Goblin", health=100):
    print(f"{name} spawned with {health} HP")

spawn_enemy()
spawn_enemy("Dragon")
spawn_enemy("Orc", 200)
#Output:
# Goblin spawned with 100 HP
# Dragon spawned with 100 HP
# Orc spawned with 200 HP