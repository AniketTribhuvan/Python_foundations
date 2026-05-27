# Vowel Counter Program

# Taking string input from user
str = input("Enter a string = ")

# Variable for counting total characters
count = 0

# Finding length of string manually
for ch in str:
    count = count + 1

# Starting index from 0
i = 0

# Variable for storing total vowels
vowel_count = 0

# Loop for checking every character
while(i < count):

    # Checking if character is a vowel
    if(str[i] in "AEIOUaeiou"):

        # Increasing vowel count
        vowel_count = vowel_count + 1

    # Moving to next character
    i = i + 1

# Printing total vowels
print("Vowel count = ", vowel_count)

# Output :
# Enter a string = Hello
# Vowel count =  2