# Taking string input from user
text = input("Enter a string : ")

# Finding length of original string manually
count = 0
for ch in text:
    count = count + 1

# Empty string to store lowercase alphabets only
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

# Finding length of cleaned string manually
count = 0
for ch in new_text:
    count = count + 1

# Empty string to store string without duplicates
text2 = ""

i = 0

# Looping through cleaned string
while i < count:

    # Checking if character already appeared before
    if new_text[i] not in new_text[:i]:

        # Adding unique character into new string
        text2 = text2 + new_text[i]

    i = i + 1

# Printing final string without duplicates
print(text2)