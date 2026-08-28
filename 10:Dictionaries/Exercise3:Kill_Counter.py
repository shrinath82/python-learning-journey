"""
> Question: Track kills: Dragon 2, Goblin 5, Orc 1.
> Steps:
> - init dict with 0
> - increment
> - print
"""

#Solution:
kills = {"Dragon":0, "Goblin":0, "Orc":0}
kills["Dragon"] += 2
kills["Goblin"] += 5
kills["Orc"] += 1
print(kills)
# Output: {'Dragon': 2, 'Goblin': 5, 'Orc': 1}

for name, count in kills.items():
    print(name, "killed:", count)
# Output:
# Dragon killed: 2
# Goblin killed: 5
# Orc killed: 1