# 11.Guess the Number Game
# Set a secret number (e.g., 7)
# Let the user guess until they get it right
# Print "Too high" or "Too low" for wrong guesses
# Print "Correct!" when guessed
while guess != secret_number:
    guess = int(input(" Enter a Guess the Number: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Congratultions! you guessed it right")
