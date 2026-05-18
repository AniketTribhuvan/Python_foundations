"""
Type casting means converting one datatype into another datatype
using functions like int(), float(), str(), etc.
"""

a = "25"        # a is a string datatype

print(a)
# Output: 25

print(type(a))
# Output: <class 'str'>

print(int(a))
# String is converted into integer using type casting.
# Output: 25

print(type(int(a)))
# Output: <class 'int'>


a = "1"
b = "2"

print(a + b)
# Output: 12
# Because both are strings, they get concatenated.

print(int(a) + int(b))
# Output: 3
# First type casting happens, then addition is performed.


"""
There are two types of type casting:

1. Explicit Type Casting
2. Implicit Type Casting

Above examples are of explicit type casting,
because the programmer manually converts the datatype.

Implicit type casting happens automatically by Python.
"""


a = 10          # Integer datatype
b = 1.2         # Float datatype

c = a + b
# Here Python automatically converts a into 10.0 (float)
# before performing addition.

print("Type of a is", type(a))
# Output: <class 'int'>

print("Type of b is", type(b))
# Output: <class 'float'>

print(c)
# Output: 11.2

print("Type of c is", type(c))
# Output: <class 'float'>