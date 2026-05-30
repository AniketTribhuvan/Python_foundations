# A function is a block of code that performs a specific task whenever it is called.

# In bigger programs, functions help to organize code
# and make programs clean and easier to manage.

# Syntax:
# def function_name(parameters):
#     # Code and statements

# Function to compare two numbers
def compare(a, b):                  # a & b are arguments which is passed to the function if required

    # Checking if a is greater
    if(a > b):
        print("a is greater than b")

    # Checking if b is greater
    elif(a < b):
        print("b is greater than a")

    # If both numbers are equal
    else:
        print("a and b are equal")

# Taking input from user
a = int(input("Enter a number  a : "))
b = int(input("Enter another number b : "))

# Calling function
compare(a, b)