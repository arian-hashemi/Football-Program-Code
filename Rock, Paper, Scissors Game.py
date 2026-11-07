
import random

print("Rock Paper Scissors")

print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")

player = int(input("Enter your choice: "))

computer = random.randint(1, 3)

if player == 1:
    print("You chose Rock")
elif player == 2:
    print("You chose Paper")
elif player == 3:
    print("You chose Scissors")
else:
    print("Invalid choice")

if player >= 1 and player <= 3:

    if computer == 1:
        print("Computer chose Rock")
    elif computer == 2:
        print("Computer chose Paper")
    else:
        print("Computer chose Scissors")

    if player == computer:
        print("It's a tie!")

    elif player == 1 and computer == 3:
        print("You win!")

    elif player == 2 and computer == 1:
        print("You win!")

    elif player == 3 and computer == 2:
        print("You win!")

    else:
        print("Computer wins!")
