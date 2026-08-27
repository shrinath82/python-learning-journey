#If you want an independent list, create a copy.

#Example
a = [1, 2]
b = a.copy()
b.append(3)

print(a)
print(b)

"""
Output
[1, 2]
[1, 2, 3]

Now modifying `b` doesn't change `a`.
"""