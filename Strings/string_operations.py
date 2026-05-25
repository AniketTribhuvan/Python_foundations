# String Operations in Python
# Detailed notes given in notes.md

# Creating two strings
str = "Hello"
str2 = "World"


# 1. Concatenation (+)
# Used to join two strings together

print(str + str2)

# Output:
# HelloWorld

# If you want space between them:
# print(str + " " + str2)

# You can only concatenate strings with strings.
# Integer + string will give error.

# print(16 + str)
# TypeError


# 2. Repetition (*)
# Used to repeat a string multiple times

print(str * 5)

# Output:
# HelloHelloHelloHelloHello

# String can only be multiplied by an integer.

# print(str * 2.5)
# TypeError


# 3. Membership Operators
# in      -> Checks if substring exists
# not in  -> Checks if substring does NOT exist

print("H" in str)

# Output:
# True

# Because "H" exists inside "Hello"


print("H" not in str)

# Output:
# False

# Because "H" is present in the string


print("A" not in str)

# Output:
# True

# Because "A" is not present in "Hello"


# 4. Comparison Operators
# Python compares strings character by character
# according to ASCII / Unicode values

print("Python" == "Python")

# Output:
# True

# Both strings are exactly same


print("python" == "Python")

# Output:
# False

# String comparisons are case-sensitive
# Small 'p' and capital 'P' are different


print("Python" != "Java")

# Output:
# True

# Because both strings are different


print("banana" > "apple")

# Output:
# True

# 'b' comes after 'a' alphabetically


print("apple" < "banana")

# Output:
# True

# 'a' comes before 'b' alphabetically


print("A" < "a")

# Output:
# True

# Comparison happens according to ASCII values
# Capital letters have smaller ASCII values
# than lowercase letters