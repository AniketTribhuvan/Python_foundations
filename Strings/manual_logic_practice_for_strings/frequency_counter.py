# Taking string input from user
text = input("Enter a string = ")

# Taking character input
char = input("Enter a character = ")

# Check if only one character is entered
if len(char) != 1:
    print("Please enter only one character")

else:
    # Finding frequency
    i = 0
    char_count = 0

    while i < len(text):

        if text[i] == char:
            char_count += 1

        i += 1

    # Printing result
    if char_count > 0:
        print("Frequency =", char_count)
    else:
        print("Character not found")