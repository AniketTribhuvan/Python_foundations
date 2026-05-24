# Personal Study Notes For Strings


# Basics of Strings

## 1. What is a String?

A string (str) is a sequence of characters written inside quotes.

Python supports:

'single quotes'

"double quotes"

"""triple quotes"""

Single/Double quotes are mostly used for one-line text.

Triple quotes are used for multi-line text.

Example:

msg = """Hello
This is line 2
This is line 3"""


## 2. Important Characteristics of Strings

Strings are immutable.

This means once a string is created, it cannot be changed directly.

Example:

name = "Aniket"

Methods like upper(), replace(), and strip()
create a new string instead of modifying the original one.


## 3. Indexing System

Every character in a string has an index position.

Indexing starts from 0.

Example:

String:   A   n   i   k   e   t
Index:    0   1   2   3   4   5

name = "Aniket"

print(name[0])   # A
print(name[3])   # k


### Negative Indexing

Python also supports negative indexing.

Example:

String:    A    n    i    k    e    t
Negative: -6   -5   -4   -3   -2   -1

print(name[-1])   # t
print(name[-2])   # e

Negative indexing is useful for accessing characters from the end.



# String Methods

## What are String Methods?

String methods are built-in functions used to perform operations on strings.

Methods are attached to objects using dot (.) notation.

Example:

text = "Hello"

print(text.upper())


## Important Point About Strings

Strings are immutable in Python.

This means original string does not change.

Methods create and return a new modified string.

Example:

text = "Hello"

print(text.upper())   # HELLO
print(text)           # Hello


## 1. upper()

Converts all characters into uppercase.

Example:

text = "hello world"

print(text.upper())   # HELLO WORLD


## 2. lower()

Converts all characters into lowercase.

Example:

text = "HELLO WORLD"

print(text.lower())   # hello world


## 3. len()

Counts total number of characters in string.

Spaces are also counted.

Example:

text = "Hello World"

print(len(text))      # 11


## 4. strip()

Removes whitespaces from both left and right side.

Example:

text = "    Hello    "

print(text.strip())   # Hello


## 5. rstrip()

Removes characters from right side only.

Example:

text = "Hello????"

print(text.rstrip("?"))   # Hello


## 6. replace()

Replaces old values with new values.

Example:

text = "Night"

print(text.replace("N", "R"))   # Right


## 7. split()

Divides string into parts and returns a list.

Example:

text = "Hello World"

print(text.split(" "))   # ['Hello', 'World']


## 8. capitalize()

Makes first letter uppercase and remaining letters lowercase.

Example:

text = "hello WORLD"

print(text.capitalize())   # Hello world


## 9. center()

Aligns string at center.

Can also fill spaces using characters.

Example:

text = "Hello"

print(text.center(20))

print(text.center(20, "!"))


## 10. count()

Returns how many times a value occurs.

Example:

text = "He is good. He is kind."

print(text.count("He"))   # 2


## 11. endswith()

Checks whether string ends with given value.

Returns True or False.

Example:

text = "Python"

print(text.endswith("on"))   # True


## 12. find()

Returns index of first occurrence.

Returns -1 if value is absent.

Example:

text = "Hello"

print(text.find("e"))   # 1


## 13. index()

Similar to find().

But gives error if value is absent.

Example:

text = "Hello"

print(text.index("e"))   # 1


## 14. isalnum()

Returns True if string contains only alphabets and numbers.

Example:

text = "Hello123"

print(text.isalnum())   # True


## 15. isalpha()

Returns True if string contains only alphabets.

Example:

text = "Hello"

print(text.isalpha())   # True


## 16. islower()

Checks whether all characters are lowercase.

Example:

text = "hello"

print(text.islower())   # True


## 17. isupper()

Checks whether all characters are uppercase.

Example:

text = "HELLO"

print(text.isupper())   # True


## 18. isprintable()

Returns True if all characters are printable.

Example:

text = "Hello"

print(text.isprintable())   # True


## 19. isspace()

Returns True only if string contains spaces.

Example:

text = "     "

print(text.isspace())   # True


## 20. istitle()

Checks whether first letter of each word is capitalized.

Example:

text = "Hello World"

print(text.istitle())   # True


## 21. startswith()

Checks whether string starts with given value.

Example:

text = "Python"

print(text.startswith("Py"))   # True


## 22. swapcase()

Converts uppercase to lowercase and lowercase to uppercase.

Example:

text = "Hello"

print(text.swapcase())   # hELLO


## 23. title()

Capitalizes first letter of every word.

Example:

text = "hello world"

print(text.title())   # Hello World


## 24. String Reversing Trick

[::-1] is used to reverse a string.

Meaning:

Start from end.

Move backward one step at a time.

Example:

text = "Hello"

print(text[::-1])   # olleH


## Difference Between find() and index()

find()

Returns -1 if value not found.

index()

Gives error if value not found.


## Important Revision Points

Strings are immutable.

Methods return new strings.

split() returns list.

[::-1] reverses string.

find() returns -1 if absent.

index() gives error if absent.



# String Operations


## 1. Concatenation (+)

Concatenation means joining two or more strings together.

Example:

a = "Hello"
b = "World"

print(a + b)

#Output:
#HelloWorld


### Adding Space Between Words

print(a + " " + b)

#Output:
#Hello World


### Important Point

Only strings can be concatenated with strings.

Example:

age = 16

print("Age: " + age)
TypeError

Correct way:

print("Age: " + str(age))


## 2. Repetition (*)

Repetition means repeating a string multiple times.

Example:

text = "Hi "

print(text * 3)

Output:
Hi Hi Hi


### Useful for Formatting

print("=" * 20)

Output:
00000000000000000000


### Important Point

String can only be multiplied by an integer.

Example:

print("A" * 2.5)
TypeError


## 3. Membership Operators

Membership operators are used to check whether
a substring exists inside another string.


### in Operator

Returns True if substring exists.

Example:

text = "Python Programming"

print("Python" in text)

Output:
True


print("Java" in text)

Output:
False


### not in Operator

Returns True if substring does not exist.

Example:

text = "Machine Learning"

print("AI" not in text)

Output:
True


print("Machine" not in text)

Output:
False


### Real Life Example

password = "python123"

print("@" in password)

Can be used in password validation systems.


## 4. Comparison Operators

Comparison operators compare two strings.

Python compares strings character by character
according to ASCII / Unicode values.


### Equal To (==)

Checks whether both strings are same.

Example:

print("Python" == "Python")

Output:
True


### Not Equal To (!=)

Checks whether strings are different.

Example:

print("Python" != "Java")

Output:
True


### Greater Than (>)

Example:

print("banana" > "apple")

Output:
True

Because 'b' comes after 'a' alphabetically.


### Less Than (<)

Example:

print("apple" < "banana")

Output:
True

Because 'a' comes before 'b' alphabetically.


### Case Sensitivity

String comparisons are case-sensitive.

Example:

print("python" == "Python")

Output:
False

Small 'p' and capital 'P' are different.


### ASCII / Unicode Comparison

Example:

print("A" < "a")

Output:
True

Capital letters have smaller ASCII values
than lowercase letters.


## Important Revision Points

+ joins strings.

* repeats strings.

in checks existence.

not in checks absence.

String comparisons are case-sensitive.

Python compares strings using ASCII / Unicode values.