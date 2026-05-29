# break statement is used to stop the loop immediately.
# When break executes, loop gets terminated.

for i in range(0,10):

    # If value of i becomes 6
    if(i == 6):

        # terminate the loop
        break

    # print value of i
    print(i)


# Output :
# 0
# 1
# 2
# 3
# 4
# 5


# Explanation :
# Loop starts from 0 and goes till 9.
# But when i becomes 6, break statement executes.
# Due to this the loop stops immediately.
# Therefore 6,7,8,9 are not printed.