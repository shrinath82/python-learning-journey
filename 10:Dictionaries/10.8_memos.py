# 10.8 Memos - Memoization
# - Store result once, reuse later

memo = {}

# Example 1: Store and reuse
memo[5] = 120 # 5! = 120
print(memo[5])
# Output: 120


# Example 2: Caching function
def get_damage(level):
    if level in memo:
        return memo[level]
    result = level * 10 + 50
    memo[level] = result
    return result

print(get_damage(10))
# Output: 150

print(get_damage(10))
# Output: 150 (from memo, not calculated again)

print(memo)
# Output: {5: 120, 10: 150}