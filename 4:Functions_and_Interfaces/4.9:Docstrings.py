#Document what a function does. RUN EVERYTHIN INDIVIDUALLY
#Example 1
def jump():
    """Player jump action."""
    print("Jump")

jump()
#Output: Jump



#Example 2 – Viewing the Documentation
def jump():
    """Player jump action."""
    print("Jump")

help(jump)


#Sample Output: 
Help on function jump:

jump()
    Player jump action.


#Example 3 – Access the Docstring Directly
def heal():
    """Restore player health."""
    print("Healing")

print(heal.__doc__)


#Output: Restore player health.

