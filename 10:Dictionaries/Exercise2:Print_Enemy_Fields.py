"""
> Question: Create Dragon enemy data and print all fields nicely.
> Steps:
> - create dict
> - print with f-string
"""

#Solution:
enemy = {"name":"Dragon","health":500,"damage":50}
print(f"{enemy['name']} | HP: {enemy['health']} | DMG: {enemy['damage']}")
# Output: Dragon | HP: 500 | DMG: 50