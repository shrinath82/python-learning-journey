#3.8-Tracebacks
def attack():
    print(damage)

attack()

"""
Output:NameError: name 'damage' is not defined EXPECTED
Python also shows the traceback indicating:
* File name
* Line number
* Function where the error occurred
"""