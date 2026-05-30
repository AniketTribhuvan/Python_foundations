# A required function argument is a parameter
# that must be provided while calling a function.

# If required argument is not passed,
# Python gives TypeError.

# Here 'a' is required argument because
# it does not have default value.
def average(a, b = 15, c = 10):

    # Printing average
    print("Average = ", (a + b + c) / 3)

# Calling function without passing argument to 'a'

# average()

# Output :
# File "file_name", line 8, in <module>
#     average()
#     ~~~~~~~^^
# TypeError: average() missing 1 required positional argument: 'a'


# Calling function with required argument
average(5)

# Output :
# Average =  10.0