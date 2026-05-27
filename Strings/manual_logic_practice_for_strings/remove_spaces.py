# Taking string input from user
text = input("Enter a string = ")

# Finding length of string manually
count = 0
for ch in text:
    count = count + 1

# Variable for loop control
i = 0

# Empty string to store string without spaces
new_text = ""

# Looping through original string
while i < count:

    # Checking if character is not space
    if(text[i] != " "):

        # Adding character into new string
        new_text = new_text + text[i]

    i = i + 1

# Finding length of new string manually
count = 0
for ch in new_text:
    count = count + 1

# Printing final string character by character
i = 0
print("string = ", end="")

while i < count:
    print(new_text[i], end="")
    i = i + 1