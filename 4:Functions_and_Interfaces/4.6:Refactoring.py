#Improve code without changing its behavior.
"""
#Before Refactoring
print("Enemy")
print("Enemy")
print("Enemy")


Output: 
Enemy
Enemy
Enemy
"""

#After Refactoring
def enemy():
    print("Enemy")

enemy()
enemy()
enemy()


#Output: 
#Enemy
#Enemy
#Enemy
#The output is identical, but the code is easier to maintain.