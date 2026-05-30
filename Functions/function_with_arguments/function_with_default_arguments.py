# 1. Default arguments :
# Arguments which are initialized in function definition
# are called default arguments.

# If function is called without arguments,
# then default values are used.

# Function with default arguments
def name(fname = "David", lname = "Clear"):

    # Printing full name
    print("Hello,", fname, lname)

# Calling function without arguments
name()

# Output :
# Hello, David Clear
# Default arguments are used here


# Calling function with 1 argument
name("John")

# Output :
# Hello, John Clear
# "John" is taken as first argument


# Calling function with both arguments
name("John", "Fincher")

# Output :
# Hello, John Fincher