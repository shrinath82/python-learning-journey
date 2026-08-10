#5.8-Nested_Conditionals
#Example 1
alive = True
weapon = True
if alive:
    if weapon:
        print("Attack")
#Example 2
logged_in = True
is_admin = False

if logged_in:
    if is_admin:
        print("Admin Panel")
    else:
        print("User Dashboard")