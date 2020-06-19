# Rock Paper Scissors Game
# Create a rock-paper-scissors game.
# Ask the player to pick rock, paper or scissors.
# Have the computer chose its move.
# Compare the choices and decide who wins.
# Print the results.
# Subgoals:
# Give the player the option to play again.
# Keep a record of the score (e.g. Player: 3 / Computer: 6).
import random

options = ('rock', 'paper', 'scissors')
player_score = 0
pc_score = 0


def get_choice():
    while True:
        inner_choice = input("Rock? Paper? Scissors?  ").lower()
        if inner_choice not in options:
            print("That is not a valid option.")
            continue
        else:
            break
    return inner_choice


while True:
    choice = get_choice()
    pc_choice = random.choice(options)

    if choice == pc_choice:
        print(f"Computer chose {pc_choice}. Game is a tie.")
    elif choice == 'rock':
        if pc_choice == 'paper':
            print(f"Computer chose {pc_choice}. You lose.")
            pc_score += 1
        else:
            print(f"Computer chose {pc_choice}. You win.")
            player_score += 1
    elif choice == 'paper':
        if pc_choice == 'scissors':
            print(f"Computer chose {pc_choice}. You lose.")
            pc_score += 1
        else:
            print(f"Computer chose {pc_choice}. You win.")
            player_score += 1
    else:
        if pc_choice == 'rock':
            print(f"Computer chose {pc_choice}. You lose.")
            pc_score += 1
        else:
            print(f"Computer chose {pc_choice}. You win.")
            player_score += 1

    q = input("Play again? (Y/N): ")
    if q == 'n' or q == 'N':
        break

print()
print(f"The score was You: {player_score} | Computer: {pc_score}")
print("Thanks for playing!")
