"""
do..while is a loop in which a set of instructions will execute at least once whether the condition is false 
and then the repetition of loop's body will depend on the condition passed at the end of the while loop.
But in python there is no do while loop as in C. So we emulate do while loop in python using python only
"""

while True:                                     # True will enter in loop
  number = int(input("Enter a number: "))
  print(number)
  if number > 38:                               # condition is check here, if condition is false then break terminates loop.
    break
  
# Output:
# Enter a number: 11
# 11
# Enter a number: 23
# 23
# Enter a number: 45
# 45