# 10.4 A Collection of Counters
# - Pattern: init to 0, then += 1

# Example 1: Simple kill counter
kills = {}
kills["dragon"] = 0
kills["dragon"] += 1
kills["dragon"] += 1
print(kills)
# Output: {'dragon': 2}


# Example 2: Multiple counters
counts = {}
counts["dragon"] = 1
counts["goblin"] = 3
counts["dragon"] += 1
print(counts)
# Output: {'dragon': 2, 'goblin': 3}