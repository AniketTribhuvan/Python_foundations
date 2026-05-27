# Reverse String Program

# Taking string input from user
str = input("Enter a string = ")

# Variable to count total characters
count = 0

# Loop for finding length of string manually
for ch in str:
    count = count + 1

# Loop runs from last character to first character
while(count > 0):

    # Printing characters in reverse order
    print(str[count - 1], end = "")

    # Decreasing count step-by-step
    count = count - 1

# Output :
# Enter a string = Hello
# olleH