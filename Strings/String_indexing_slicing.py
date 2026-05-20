"""
String index means the position of the character in string which starts in sequence from 0.

String slice means a portion of a string.

String slicing is used to access a specific part
of a string.

Syntax:
variable[start_index : end_index]

Note:
The ending index is not included in the output.
Python prints characters only up to (end_index - 1).
"""

name = "Aniket"

# Index positions:
# A = 0, n = 1, i = 2, k = 3, e = 4, t = 5


print(name[0:6])
# Output: Aniket
# Prints characters from index 0 to 5.

print(name[1:5])
# Output: nike
# Prints characters from index 1 to 4.


"""
Python can automatically take starting or ending index
if left blank.

This is called:
- Omit Start
- Omit Stop
"""

print(name[:6])
# Output: Aniket
# Start index is automatically taken as 0.

print(name[0:])
# Output: Aniket
# End index is automatically taken till the end of string.