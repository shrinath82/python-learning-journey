#A variable refers to an object.

#Example 1 – List Type
inventory = ["Sword"]
print(type(inventory))


#Output: <class 'list'>


#Example 2 – String Is Also an Object
name = "Krishna"
print(type(name))

#Output: <class 'str'>


#Example 3 – Different Objects
number = 100
text = "Python"
items = ["Sword", "Shield"]

print(type(number))
print(type(text))
print(type(items))


"""
Output
<class 'int'>
<class 'str'>
<class 'list'>
The important idea from this section is:
variable → object

For example:
inventory → list object
name      → string object
score     → integer object
"""