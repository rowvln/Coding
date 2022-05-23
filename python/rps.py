import random # imports the random module

player_wins = 0 # tracks the number of times player won
computer_wins = 0 # tracks the number of times computer won
winning_score = int(input("How many rounds would you like to play? ")) # asks the user how many rounds user wants to be played

# while the score is less than the rounds the user wants to play, keep playing. otherwise print out who wins
while player_wins < winning_score and computer_wins < winning_score:

    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")

    rand_num = random.randint(0,2) # set rand_num equal to the a random number between 0 and 2

    player = input("Player 1, make your move. (rock/paper/scissors): ").lower()

    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer has picked {computer}!")

    # main program
    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("player has won the round.")
        player_wins += 1
    elif player == "paper" and computer == "rock":
        print("player has won the round.")
        player_wins += 1
    elif player == "scissors" and computer == "paper":
        print("player has won the round.")
        player_wins += 1
    else:
        print("computer has won the round.")
        computer_wins += 1

if player_wins > computer_wins:
    print("\nCONGRATS, YOU WON!!")
elif player_wins == computer_wins:
    print("\nITS A TIE!!")
else:
    print("\nOH NO, THE COMPUTER WON!!")

print(f"\nFINAL SCORE - Player Score: {player_wins} Computer Score: {computer_wins}")