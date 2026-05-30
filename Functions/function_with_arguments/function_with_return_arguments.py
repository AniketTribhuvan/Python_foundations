# The return statement sends a value
# back from function to where it was called.

# *nums stores multiple arguments inside a tuple
def average(*nums):

  # Printing type of nums
  print("Type of nums is :", type(nums))

  # Variable to store sum
  sum = 0

  # Looping through all numbers
  for i in nums:
     sum = sum + i

  # Returning average
  return sum / len(nums)

# Storing returned value into variable
avg = average(1, 2, 3, 4)

# Printing final average
print("Average is:", avg)

# Output :
# Type of nums is : <class 'tuple'>
# Average is: 2.5