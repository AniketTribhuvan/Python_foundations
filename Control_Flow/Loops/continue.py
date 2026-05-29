# continue statement is used to skip the current iteration.
# It does not terminate the loop like break.

for i in range(0,10):

    # If value of i becomes 6
    if(i == 6):

        # skip current iteration
        continue

    # print value of i
    print(i)


# Output :
# 0
# 1
# 2
# 3
# 4
# 5
# 7     # 6 is skipped
# 8
# 9


# Explanation :
# Loop starts from 0 and goes till 9.
# But when i becomes 6, continue statement executes.
# Due to this print(i) is skipped only for that iteration.
# Then loop directly moves to next iteration.
# Therefore 6 is not printed.