# Text Analyzer Mini Project

# In this project, user enters a paragraph or sentence.
# Then program analyzes the text and gives different outputs.


# Features of this project:
# 1. Total characters
# 2. Total words
# 3. Total vowels
# 4. Total consonants
# 5. Uppercase letters count
# 6. Lowercase letters count
# 7. Reversed text


# Taking input from user
text = input("Enter text = ")


# Variables
i = 0
word_count = len(text.split())
vowel_count = 0
consonant_count = 0
uppercase_count = 0
lowercase_count = 0


# Loop will run through every character of string
for char in text:


    # Checking only alphabets
    # because numbers and symbols are not vowels/consonants
    if text[i].isalpha():


        # Checking vowels
        if text[i] in "AEIOUaeiou":
            vowel_count = vowel_count + 1


        # If alphabet is not vowel then it is consonant
        else:
            consonant_count = consonant_count + 1


    # Counting uppercase letters
    if text[i].isupper():
        uppercase_count = uppercase_count + 1


    # Counting lowercase letters
    elif text[i].islower():
        lowercase_count = lowercase_count + 1


    # Moving to next index
    i = i + 1


# Final Outputs
print("Total characters = ", len(text))
print("Total words = ", word_count)
print("Total vowels = ", vowel_count)
print("Total consonants = ", consonant_count)
print("Uppercase count = ", uppercase_count)
print("Lowercase count = ", lowercase_count)
print("Reversed text = ", text[::-1])