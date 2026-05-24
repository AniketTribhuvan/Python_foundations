# MY PYTHON BASICS REFERENCE LOG
# Just putting all my theory notes, rules, and logic explanations in one place 
# so I don't forget how Python actually handles data, math, and inputs.


# WHAT EVEN IS PYTHON?

Basically, Python is a high-level, interpreted programming language. 

* High level = The code actually looks like normal English. We don’t have to 
  stress about manual hardware memory addresses or dealing with crazy CPU registers.
* Interpreted = The computer reads and runs the code line-by-line using the 
  Python Interpreter. It doesn't compile everything into a massive binary file 
  before running. This makes testing super fast, but it means if you have a typo 
  on line 50, you won't find out until the code actually hits line 50 and crashes.


2. VARIABLES AND HOW MEMORY WORKS

# Variable Assignment
In Python, a variable isn't a physical box that holds data. It's more like a 
name tag (a pointer) that hooks onto an object sitting in the computer's memory.

* If I write x = 5, Python creates an integer object 5 somewhere in memory, 
  and then slaps the label x onto it.
* If I change it later to x = "Hello", the label x just unties itself from 
  the 5 and hooks onto a brand new string object "Hello".

## Dynamic Typing
Python uses means you don't have to declare datatype of variable like C/C++. Python will 
automatically figures out the typetype from the value of variable you give.
"""
### You can check what a variable currently is using the type() function:
x = 5
print("x is currently:", type(x))  # <class 'int'>

x = "Hello"
print("x is now:", type(x))       # <class 'str'>


3. THE MAIN DATA TYPES (CORE PRIMITIVES)

These are the basic building blocks Python uses for data:

my_int = 10           # Integers (int): Normal whole numbers, no decimals
my_float = 3.14       # Floats (float): Numbers with decimal points or fractions
my_str = "Python"     # Strings (str): Text wrapped in quotes
my_bool = True        # Booleans (bool): True or False flags. Caps matter! (`true` breaks)


4. INPUT AND OUTPUT MECHANICS

### Printing Stuff: print()
The print() function just print the data onto the console screen. You can tweak 
how it looks using a couple of cool optional settings like `sep` and `end`.
"""
### `sep` changes what goes between items (default is a space)
print("Apple", "Banana", "Cherry", sep=" | ") 
Output : Apple | Banana | Cherry

### `end` changes what happens at the very end (default is a newline `\n`)
print("This stays on the ", end="")
print("This stays on the ")


### Getting Input: input()
The input() function pauses the program and waits for the user to type something.
CRITICAL RULE: Without declaring type It always treats whatever the user types as a string (text).
"""
# user_age = input("Enter your age: ") # If they type 17, it saves as "17" (text)


5. TYPE CASTING (CONVERTING DATA)

Since input() only gives us strings, we have to manually swap data types around 
if we want to do any actual math. This is called Type Casting.

# Implicit Conversion: Python does this automatically to prevent losing data.
automatic_swap = 5 + 2.0  # An int + a float automatically results in a float (7.0)

# Explicit Conversion: Forcing a type change yourself using built-in functions:
text_num = "10"
actual_num = int(text_num)     # Turns the text string "10" into math number 10
decimal_num = float(5)         # Turns the integer 5 into 5.0
back_to_text = str(12.3)       # Turns the decimal number into text string "12.3"


6. OPERATORS CHEAT SHEET

# Math Operators

print(10 + 3)   # Addition -> 13
print(10 - 3)   # Subtraction -> 7
print(10 * 3)   # Multiplication -> 30
print(10 / 2)   # True Division -> Always gives back a float decimal (2.0)
print(10 // 3)  # Floor Division -> Divides and chops off the decimal, rounding down (3)
print(10 % 3)   # Modulo -> Tells you the remainder of a division (1)
print(2 ** 3)   # Exponentiation -> Powers/Exponents (2 cubed = 8)


#  Comparison Operators (Always answers True or False)

print(5 == 5)   # Equal to -> True
print(5 != 2)   # Not equal to -> True
print(5 > 3)    # Greater than -> True
print(5 <= 3)   # Less than or equal to -> False


# Logical Operators (Chaining comparisons together)
* and: Only True if BOTH sides are true. If the first part is False, Python 
       stops checking entirely (short-circuit evaluation) because it's already ruined.
* or:  True if AT LEAST ONE side is true.
* not: Flips the boolean value.

print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 7. MISTAKES I KEEP MAKING (THE LOG)

## Mistake 1: The String Trap
## If you forget to type-cast input, Python glues strings instead of doing math.

num1 = "5"  # Simulated input("Enter 5: ")
num2 = "5"  # Simulated input("Enter 5: ")
print("Broken Addition:", num1 + num2) # Spits out "55" instead of 10. Annoying.

## The Fix:
print("Fixed Addition:", int(num1) + int(num2)) # Outputs 10