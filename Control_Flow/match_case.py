"""
Match case is used when we have to execute one case among multiple cases.

1. We declare a variable for match
2. if a case matches the variable then the case is executed & interpreter comes out of the match case
3. If no case matches the variable then default case (case _) is executed.

Match case is same as switch case in C.
"""

# Example
# Voting Eligibility Program

age = int(input("Enter your age = "))

if(age >= 18):

    print("You're eligible to vote.")

    print("""
Options:
1. Party A
2. Party B
3. Party C
4. Party D
""")

    op = int(input("Enter your option = "))

    match op:

        case 1:
            print("You chose Party A")

        case 2:
            print("You chose Party B")

        case 3:
            print("You chose Party C")

        case 4:
            print("You chose Party D")

        case _:
            print("Invalid option")

else:
    print("You're not eligible to vote.")