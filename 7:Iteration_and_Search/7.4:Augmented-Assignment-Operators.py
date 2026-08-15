#provides shorter versions of common updates.
#Example 1 – `+=`
count = 0

for i in range(5):
    count += 1

print(count)

#Output: 5
#Equivalent to: count = count + 1


#Example 2 – `-=`
count = 10

for i in range(3):
    count -= 1

print(count)

#Output: 7


#Example 3 – `*=`
count = 2

for i in range(3):
    count *= 2

print(count)

#Output: 16


#Example 4 – `/=`
count = 100

for i in range(2):
    count /= 2

print(count)

#Output: 25.0


#Example 5 – `//=`
count = 100

for i in range(2):
    count //= 3

print(count)

#Output: 11


#Example 6 – `%=`
count = 20

for i in range(2):
    count %= 6

print(count)

#Output: 2


#Example 7 – `=`
count = 2

for i in range(3):
    count **= 2

print(count)

#Output: 256