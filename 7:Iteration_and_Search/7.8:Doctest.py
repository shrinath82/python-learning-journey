#A doctest places an executable example inside a function's documentation.
#Example 1 – Basic Doctest

def square(x):
    """
    >>> square(4)
    16
    """
    return x * x

#To actually execute the embedded test:

import doctest

def square(x):
    """
    >>> square(4)
    16
    """
    return x * x

doctest.testmod()

"""
Output

If the test passes: No output means the test succeeded.
"""

#Example 2 – Multiple Doctests
import doctest
def add(a, b):
    """
    >>> add(2, 3)
    5

    >>> add(10, 20)
    30
    """
    return a + b

doctest.testmod(verbose=True)

"""
Output: 
Trying:
    add(2, 3)
Expecting:
    5
ok
Trying:
    add(10, 20)
Expecting:
    30
ok
1 items passed all tests
2 tests in 1 items.
2 passed and 0 failed.
Test passed.
"""

#Example 3 – Failed Doctest
import doctest
def square(x):
    """
    >>> square(4)
    20
    """
    return x * x

doctest.testmod()

#Output: reports a failed test because the actual result is `16`, not `20`.

"""
Note:
"""
That error is intentional in the example I gave for 7.8 – Doctest, Example 3.

Your doctest says:
def square(x):
    """
    >>> square(4)
    20
    """
    return x * x


calculates: 4 × 4 = 16
But the doctest says it expects: 20

So `doctest` correctly reports:

Expected: 20

Got: 16

#Correct version
Change `20` to `16`:
import doctest
def square(x):
    """
    >>> square(4)
    16
    """
    return x * x
doctest.testmod()

Now run: 3 "7.8:Doctest.py"
If everything is correct, **there should be no output**. That means the doctest passed.

#What you just learned
A doctest compares:

Your function's actual result
          ↓
        16
          ↓
Expected result written in docstring
          ↓
        16


If they match → **PASS**

If they don't match → **FAIL**
So your  installation and `doctest` are working correctly. The problem was simply that the expected value `20` was deliberately wrong in that example to demonstrate a **failed doctest**.
"""
"""