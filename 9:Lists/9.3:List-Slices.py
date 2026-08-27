#List slicing works similarly to string slicing.

#Example 1 – Basic Slice
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

#Output: [20, 30, 40]

#Example 2 – First Three Items
scores = [100, 200, 300, 400, 500]
print(scores[:3])

#Output: [100, 200, 300]

#Example 3 – From an Index to the End
items = ["Sword", "Shield", "Potion", "Key"]
print(items[2:])

#Output: ['Potion', 'Key']

#Example 4 – Last Two Items
items = ["Sword", "Shield", "Potion", "Key"]
print(items[-2:])

#Output: ['Potion', 'Key']

#Example 5 – Reverse a List
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])

#Output: [5, 4, 3, 2, 1]