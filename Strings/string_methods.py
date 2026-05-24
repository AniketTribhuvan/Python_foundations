"""
Here we are going to study some built-in string methods used to modify strings.

A method is basically a function attached to an object.

Note:
Strings are immutable in Python. String methods create a new string
instead of changing the original one.
"""

text = "Hello World"

print(text.upper())      # upper() converts all characters into uppercase.
# Output: HELLO WORLD

print(text)              # Original string remains unchanged.
# Output: Hello World

print(text.lower())      # lower() converts all characters into lowercase.
# Output: hello world

print(len(text))         # len() counts the length of string (no. of characters)
# Output : 11

text = "   Hey How are you ????    "

print(text.strip())      # strip() removes whitespaces from both sides.
# Output: Hey How are you ????


text = "Hey How are you ????"

print(text.rstrip("?"))  # rstrip() removes trailing characters.
# Output: Hey How are you 


text = "Night"

print(text.replace("N", "R"))    # replace() replaces existing values with new ones.
# Output: Right


text = "Hello World"

print(text.split(" "))   # split() divides the string and returns a list.
# Output: ['Hello', 'World']

print(text.capitalize()) # capitalize() makes first character uppercase and rest lowercase.
# Output: Hello world

print(text.center(50))   # center() aligns the string at the center.
# Output:                    Hello World                    

print(text.center(50, "!"))  # It can also fill spaces with given characters.
# Output: !!!!!!!!!!!!!!!!!!!Hello World!!!!!!!!!!!!!!!!!!!!


text = "He is a boy. He is so kind."

print(text.count("He"))  # count() returns how many times a value occurs.
# Output: 2

print(text.endswith("kind."))  # Checks whether string ends with given value.
# Output: True

print(text.endswith("s", 1, 5))
# Checks within a given range.
# Output: True

print(text.find("kind"))
# find() returns the index of first occurrence.
# If value is not found, it returns -1.
# Output: 22

print(text.index("kind"))
# Same as find(), but gives error if value is absent.
# Output: 22

# print(text.index("rich"))
# This will give an error because "rich" is not present.


text = "Hello"

print(text.isalnum())
# isalnum() checks whether string contains only alphabets and numbers.
# Output: True

print(text.isalpha())
# isalpha() checks whether string contains only alphabets.
# Output: True

print(text.islower())
# islower() checks whether all characters are lowercase.
# Output: False

print(text.isprintable())
# isprintable() returns True if all characters are printable.
# Output: True

print(text.isspace())
# isspace() returns True only if string contains whitespaces.
# Output: False

print(text.istitle())
# istitle() checks whether first letter of each word is capitalized.
# Output: True

print(text.isupper())
# isupper() checks whether all characters are uppercase.
# Output: False


text = "Hi, How are you ?"

print(text.startswith("Hi"))        # startswith() checks whether string starts with given value.
# Output: True

print(text.swapcase())              # swapcase() converts uppercase to lowercase and vice versa.
# Output: hI, hOW ARE YOU ?

print(text.title())                 # title() capitalizes first letter of each word.
# Output: Hi, How Are You ?

text1 = "Hello"
text2 = "World"
print(text1 + text2)                # "+" concat both strings
# Output : HelloWorld

print(text1*10)                     # "*" repeat string declared no. of times.
# output : HelloHelloHelloHelloHelloHelloHelloHelloHelloHello

# Trick to reverse a string

text = "Hello world"
print(text[::-1])           # Start from the end & Move backward one position at a time
# Output : dlrow olleH      # 5 -> 4 -> 3 -> 2 -> 1 -> 0