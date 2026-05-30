# In keyword arguments, values are passed using key = value format.

# Order of arguments does not matter here
# because interpreter identifies arguments using keys.

# Function with 3 parameters
def values(a, b, c):

    # Printing values
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

# Calling function using keyword arguments
values(b=5, c=10, a=15)

# Output :
# a =  15
# b =  5
# c =  10