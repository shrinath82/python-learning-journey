"""
> Question: Create player = {"name":"Hero","health":100,"score":0} Display all values.
> Steps:
> - create dict
> - loop items
"""


#Solution:
player = {"name":"Hero","health":100,"score":0}
for k, v in player.items():
    print(k, "->", v)
# Output:
# name -> Hero
# health -> 100
# score -> 0