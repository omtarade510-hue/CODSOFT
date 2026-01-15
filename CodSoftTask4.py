# ROCK-PAPER-SCISSOR GAME

'''User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and
feedback.'''



import random

# Choices
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

print(" Welcome to Rock-Paper-Scissors Game")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock\n")

while True:
    # User input
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    # Computer selection
    computer_choice = random.choice(choices)

    # Display choices
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You Win! 🎉")
        user_score += 1

    else:
        print("Result: You Lose ")
        computer_score += 1

    # Display score
    print("Score → You:", user_score, "| Computer:", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break

    print()
