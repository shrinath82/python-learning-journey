#3.7-Stack_Diagram
#Example 1
"""
def enemy():
    print("Enemy Spawned")

def game():
    enemy()

game()

Output:Enemy Spawned


Call Stack:
game()
   │
   ▼
enemy()
"""

"""
#Example2
def c():
    print("Running")

def b():
    c()

def a():
    b()

a()

Output: Running

Call Stack
a()
 │
 ▼
b()
 │
 ▼
c()
"""