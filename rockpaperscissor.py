import random

print("🎮 Welcome to Rock, Paper, Scissors 🎮")

# Available choices
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

while True:
    print("\nPlease choose: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    # Validate input
    if user_choice not in choices:
        print("❌ Invalid choice! Please select rock, paper, or scissors.")
        continue

    # Computer random choice
    computer_choice = random.choice(choices)

    print(f"🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("😐 It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("💔 You Lose!")
        computer_score += 1

    # Show scores
    print(f"📊 Score -> You: {user_score} | Computer: {computer_score}")

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n🏁 Final Score -> You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing! 👋")
        break





