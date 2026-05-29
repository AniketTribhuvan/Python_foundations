# Secret number for guessing
secret_number = 18

# Variable to store user guess
guess = 0

# Variable to count attempts
attempt = 1

# Starting message
print("Welcome to the number guessing game!")

# Loop runs until correct number is guessed
while guess != secret_number:

  # Printing current attempt number
  print("Attempt : ", attempt)

  # Taking number input from user
  guess = int(input("Enter a number: "))

  # Checking if guess is correct
  if guess == secret_number:

    # Winning message
    print("Correct number, You won in", attempt, "attempts!")

  # If guessed number is greater
  elif guess > secret_number:
    print("Correct number is less than your number")

  # If guessed number is smaller
  else:
    print("Correct number is greater than your number")

  # Increasing attempt count
  attempt = attempt + 1