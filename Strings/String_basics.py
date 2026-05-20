"""
A string is a sequence of characters written inside
single or double quotation marks.

Example:
"Aniket" -> A, n, i, k, e, t

Index means the position of characters in a string.
Indexing starts from 0 in Python.

Example:

String :  A  n  i  k  e  t
Index  :  0  1  2  3  4  5

Purpose of indexing:
We can access individual characters of a string
and perform different operations on them.
"""

name = "Aniket"     # String written using double quotes
name = 'Aniket'     # String can also be written using single quotes

print(name[3])
# Output: k
# Accessing character using index.


"""
If we try to access an index that does not exist,
Python gives an IndexError.
"""

# print(name[8])
# This will give an error because index 8 is out of range.


"""
A multi-line string is a string that spans across
multiple lines.

It is written using triple quotes.
"""

a = """String is a sequence of characters written
inside quotation marks.

Index starts from 0 in Python.

We can use indexing to access characters
from a string."""

print(a)