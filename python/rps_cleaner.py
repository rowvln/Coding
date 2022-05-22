print("Rock....")
print("Paper....")
print("Scissors....")

p1 = input("Player 1, make your move: ")
p2 = input("Player 2, make your move: ")
 
if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("p2 wins")