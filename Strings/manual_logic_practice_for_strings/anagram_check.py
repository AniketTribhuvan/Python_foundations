# If a string is formed by rearranging all letters of other string
# that means the string is anagram of other string.
# eg. listen is anagram of silent.
# Taking two string inputs from user
text1 = input("Enter a string = ")
text2 = input("Enter another string = ")

# Variables to store lengths of strings
count1 = 0
count2 = 0

# Finding length of first string manually
for ch in text1:
    count1 = count1 + 1

# Finding length of second string manually
for ch in text2:
    count2 = count2 + 1

# Variables for loop and checking
i = 0
flag = 0

# Checking if both strings have same length
if(count1 == count2):

    # Looping through first string
    while i < count1:

        # Checking if character exists in second string
        if(text1[i] in text2):
            flag = 0

        else:
            flag = 1
            break

        i = i + 1

else:
    flag = 1

# Printing result
if(flag == 0):
     print("Anagram")

else:
    print("Not Anagram")