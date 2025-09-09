print("Welcome to Rock-Paper-Scissors! Best of 5 rounds.")

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Try again.")
        round_num -= 1
        continue
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    if winner == "user":
        user_score += 1
        print("You win this round!")
    elif winner == "computer":
        computer_score += 1
        print("Computer wins this round!")
    else:
        print("It's a tie!")

print(f"\nFinal Score: You {user_score} - Computer {computer_score}")
if user_score > computer_score:
    print("You win the game! 🎉")
elif computer_score > user_score:
    print("Computer wins! Better luck next time.")
else:
    print("It's a draw!")
