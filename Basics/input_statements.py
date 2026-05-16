"""
input() is a built-in function used to take data from the user
through the keyboard.

The text written inside input() is shown to the user as a message.

Purpose:
Learning how input works in Python.
"""

a = input("Enter first number = ")      # Suppose user enters 5
b = input("Enter second number = ")     # Suppose user enters 10

print(a + b)
# Output: 510


"""
This happens because Python takes input as a string by default.

So instead of adding numbers mathematically,
it joins them together (concatenation).

Example:
"5" + "10" = "510"
"""

a = int(input("Enter 1st number = "))
# Here input is converted into integer datatype.

b = int(input("Enter 2nd number = "))

print(a + b)

# Output: 15
# Now actual addition takes place.