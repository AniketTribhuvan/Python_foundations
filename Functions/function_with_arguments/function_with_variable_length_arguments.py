# Variable-length argument functions can accept
# any number of arguments.

# There are two types of variable-length arguments :

# 1. Arbitrary Arguments :
# Use * before parameter name while defining function.
# Arguments are stored in tuple form.

# I have not fully learned tuple and dictionary yet,
# but I know basic idea so studied these arguments also.

# Function using arbitrary arguments
def average(*nums):

  # nums is stored as tuple
  print("Type of nums is :", type(nums))

  # Variable to store sum
  sum = 0

  # Looping through all arguments
  for i in nums:
     sum = sum + i

  # Printing average
  print("Average is:", sum / len(nums))

# Calling function with multiple arguments
average(1, 2, 3, 4)

# Output :
# Type of nums is : <class 'tuple'>
# Average is: 2.5



# 2. Keyword Arbitrary Arguments :
# Use ** before parameter name while defining function.
# Arguments are stored in dictionary form.

# Function using keyword arbitrary arguments
def name(**name):

   # name is stored as dictionary
   print("Type of nums is :", type(name))

   # Accessing dictionary values using keys
   print("Name is", name["fname"], name["lname"])

# Passing arguments using key = value
name(fname = "John", lname = "David")

# Output :
# Type of nums is : <class 'dict'>
# Name is John David