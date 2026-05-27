# Taking string input from user
text = input("Enter a string : ")

# Finding length of original string manually
count = 0
for ch in text:
    count = count + 1

# Empty string to store cleaned lowercase text
new_text = ""

i = 0

# Looping through original string
while i < count:

    # Checking if character is alphabet
    if text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":

        # Converting uppercase into lowercase
        if text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_text = new_text + chr(ord(text[i]) + 32)

        # Adding lowercase character directly
        else:
            new_text = new_text + text[i]

    i = i + 1

# Finding length of new string manually
count = 0
for ch in new_text:
    count = count + 1

# Looping through cleaned string
i = 0
while i < count:

    # Checking duplicate characters
    if new_text[i] in new_text[i + 1 :] and new_text[i] not in new_text[:i]:

        # Printing duplicate character
        print(new_text[i], "is duplicate")

    i = i + 1