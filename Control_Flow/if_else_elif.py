# if-else-elif
# Used when their are multiple conditions.

a = 100
b = 1000
c = 120


if(a>b):
    if(a>c):
        print("a is greater.")
    else:
        print("c is greater")
else:
    if(b>c):
        print("b is greater.")
    else:
        print("c is greater.")

# In above program we're finding greatest number about three numbers.
# In the program we have used nested if-else & if-else-elif to reduce code & improve logic.

# 1. if a>b & a>c a is greater.
# 2. if a>b but not c then c is greater
# if a is not greater than b then it comes to main else
# then if b>c then b is greater else c is greater.