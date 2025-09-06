'''
WORKFLOW OF THE PROJECT
1-Input form the user (rock,paprer,scoissor)
2-computer choice (computer will choose randomly not conditionally)
3-print Result

CASES:
A- Rock
Rock - Rock = Tie
Rock - Paper = Paper Win
Rock - Scissor = Rock Win

B-Paper
Paper - Rock = Paper
Paper - Paper = tie
paper - Scissor = Scissor Win

C- Scissor
Scissor - Rock = Rock
Scissor - paper = Scissor
Scisoor - Scissor = tie
'''
import random

item_list = ["Rock", "Paper", "Scissor"]

while True:
    user_choice = input("\nEnter your move (Rock, Paper, Scissor) or Q/q to quit:---").capitalize()
    
    if user_choice == "Q":
        print("Game Over! Thanks for playing 😊")
        break

    if user_choice not in item_list:
        print("Invalid choice! Please choose Rock, Paper, or Scissor.")
        continue

    comp_choice = random.choice(item_list)
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("Both choose the same: Match Tie!")

    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock = Computer wins!")
        else:
            print("Rock smashes Scissor = You win!")

    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("Scissor cuts Paper = Computer wins!")
        else:
            print("Paper covers Rock = You win!")

    elif user_choice == "Scissor":
        if comp_choice == "Paper":
            print("Scissor cuts Paper = You win!")
        else:
            print("Rock smashes Scissor = Computer wins!")


