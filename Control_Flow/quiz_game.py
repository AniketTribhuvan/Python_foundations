# Welcome messages
print("Welcome to the Quiz Game!")
print("You will be asked 5 questions. Each question has 4 options.")
print("Enter the correct option (a, b, c, or d) for each question.")
print("Let's begin!\n")

# Variable to count attempts
attempt = 0

# Main game loop
while True:

    # Resetting score for every new attempt
    score = 0

    # Increasing attempt count
    attempt = attempt + 1

    print("Attempt :", attempt)

    # ---------------- Question 1 ----------------

    print("\nQuestion 1: What does AI stand for ?")
    print("a) Artificial Intelligence")
    print("b) Advanced Intelligence")
    print("c) Automated Intelligence")
    print("d) Artificial Information")

    # Taking answer input
    ans = input("Your answer: ")

    # Checking valid input
    while ans.lower() != "a" and ans.lower() != "b" and ans.lower() != "c" and ans.lower() != "d":
        print("Invalid input.")
        ans = input("Enter valid answer:")

    else:

        # Checking correct answer
        if(ans.lower() == "a"):
            print("Correct.")
            score = score + 1

        else:
            print("Incorrect. Correct answer is a) Artificial Intelligence")



    # ---------------- Question 2 ----------------

    print("\nQuestion 2: Who is known as the father of computers ?")
    print("a) Elon Musk")
    print("b) Alan Turing")
    print("c) Charles Babbage")
    print("d) Nikola Tesla")

    ans = input("Your answer: ")

    # Checking valid input
    while ans.lower() != "a" and ans.lower() != "b" and ans.lower() != "c" and ans.lower() != "d":
        print("Invalid input.")
        ans = input("Enter valid answer:")

    else:

        # Checking correct answer
        if(ans.lower() == "c"):
            print("Correct.")
            score = score + 1

        else:
            print("Incorrect. Correct answer is c) Charles Babbage")



    # ---------------- Question 3 ----------------

    print("\nQuestion 3: Which language is most popular in AI/ML ?")
    print("a) Java")
    print("b) HTML")
    print("c) C")
    print("d) Python")

    ans = input("Your answer: ")

    # Checking valid input
    while ans.lower() != "a" and ans.lower() != "b" and ans.lower() != "c" and ans.lower() != "d":
        print("Invalid input.")
        ans = input("Enter valid answer:")

    else:

        # Checking correct answer
        if(ans.lower() == "d"):
            print("Correct.")
            score = score + 1

        else:
            print("Incorrect. Correct answer is d) Python")



    # ---------------- Question 4 ----------------

    print("\nQuestion 4: Which company created ChatGPT?")
    print("a) Anthropic")
    print("b) Google")
    print("c) OpenAI")
    print("d) Perplexity")

    ans = input("Your answer: ")

    # Checking valid input
    while ans.lower() != "a" and ans.lower() != "b" and ans.lower() != "c" and ans.lower() != "d":
        print("Invalid input.")
        ans = input("Enter valid answer:")

    else:

        # Checking correct answer
        if(ans.lower() == "c"):
            print("Correct.")
            score = score + 1

        else:
            print("Incorrect. Correct answer is c) OpenAI")



    # ---------------- Question 5 ----------------

    print("\nQuestion 5: Which branch of AI focuses on training models using data?")
    print("a) Web Development")
    print("b) Machine Learning")
    print("c) UI Design")
    print("d) Cybersecurity")

    ans = input("Your answer: ")

    # Checking valid input
    while ans.lower() != "a" and ans.lower() != "b" and ans.lower() != "c" and ans.lower() != "d":
        print("Invalid input.")
        ans = input("Enter valid answer:")

    else:

        # Checking correct answer
        if(ans.lower() == "b"):
            print("Correct.")
            score = score + 1

        else:
            print("Incorrect. Correct answer is b) Machine Learning")



    # ---------------- Final Result ----------------

    # Calculating percentage
    percentage = score * 20

    print("Test Completed.")

    # Checking performance
    if(percentage > 60):
        print("Great! You score =", score)
        print("Percentage =", percentage)

    elif(percentage < 60):
        print("You score =", score)
        print("Percentage =", percentage)
        print("Better Luck Next Time")

    else:
        print("Good! You score =", score)
        print("Percentage =", percentage)

    # Asking user to play again
    play_again = input("Do you want to play again (Type yes or no): ")

    # Validating input
    while play_again.lower() != "yes" and play_again.lower() != "no":
        play_again = input("Invalid input. Enter again Do you want to play again (Type yes or no): ")

    else:

        # Ending game if user enters no
        if(play_again.lower() == "no"):
            break