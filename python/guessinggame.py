import random # imports random module to use randint

random_number = random.randint(1, 10) # randomly generates a number between 1 to 10

# handle user guesses
#   if they guess correct, tell them they won
#       otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!
guess = None

while True:
    # use a try-except block to catch entries that aren't integers which is needed for this program
    try:
        guess = int(input("Guess a number between 1 and 10 : "))
        if guess < random_number:
            print("Too low, try again!")
        elif guess > random_number:
            print("Too high, try again!")
        else:
            print("You guessed it! You won!")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == "y":
                random_number = random.randint(1, 10) # randomly generates a number between 1 to 10
                guess = None
            else:
                print("Thank you for playing!")
                break
    except ValueError as e:
        print("That is not a number. Please try again!")
