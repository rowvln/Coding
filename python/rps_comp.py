import random # imports the random module

rand_num = random.randint(0,2) # set rand_num equal to the a random number between 0 and 2

player = input("Player 1, make your move: ").lower()

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
    print("player wins")
elif player == "paper" and computer == "rock":
    print("player wins")
elif player == "scissors" and computer == "paper":
    print("player wins")
else:
    print("computer wins")