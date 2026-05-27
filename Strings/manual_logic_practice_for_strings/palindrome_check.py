# Palindrome Checker Program

# Taking string input from user
str = input("Enter a string = ")

# Variable for counting total characters
count = 0

# Finding length of string manually
for ch in str:
    count = count + 1

# Starting index from beginning
i = 0

# Variable for checking palindrome condition
flag = 0

# Loop runs till middle of string
while(i < int(count / 2)):

    # Comparing first and last characters
    if(str[i] != str[count - 1]):

        # If characters are not same
        # then string is not palindrome
        flag = 1

    else:

        # Characters matched
        flag = 0

    # Moving forward index
    i = i + 1

    # Moving backward index
    count = count - 1

# Final checking
if(flag == 0):
    print("Palindrome")

else:
    print("No")

# Output :
# Enter a string = Madam
# Palindrome