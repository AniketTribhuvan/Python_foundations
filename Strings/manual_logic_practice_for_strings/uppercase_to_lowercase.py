# Taking string input from user
text = input("Enter a string = ") 

# Finding length of string manually
count = 0
for ch in text:
    count = count + 1

# Variables for loop and new string
i = 0
new_text = ""

# Looping through string
while i < count:

    # Checking if character is uppercase
    if(text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):

        # Converting uppercase into lowercase using ASCII values
        new_text = new_text + chr(ord(text[i]) + 32)

    else:

        # Adding character as it is
        new_text = new_text + text[i]

    i = i + 1

# Printing final lowercase string
print("Lowercase text =", new_text)