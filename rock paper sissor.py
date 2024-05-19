import random

choices = {"R": "rock", "P": "paper", "S": "scissors"}
rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif rules[choice1] == choice2:
        return "Choice 1 wins!"
    else:
        return "Choice 2 wins!"

def computer_vs_player():
    player_input = input("Enter your choice (R for rock, P for paper, S for scissors): ").upper()
    if player_input not in choices:
        return "Invalid choice! Please select R, P, or S."
    
    player_choice = choices[player_input]
    computer_choice = random.choice(list(choices.values()))
    print(f"Player choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    return result

def computer_vs_computer():
    computer1_choice = random.choice(list(choices.values()))
    computer2_choice = random.choice(list(choices.values()))
    
    print(f"Computer 1 choice: {computer1_choice}")
    print(f"Computer 2 choice: {computer2_choice}")
    
    result = determine_winner(computer1_choice, computer2_choice)
    return result

def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Choose a mode:")
    print("1. Computer vs Player")
    print("2. Computer vs Computer")
    
    mode = input("Enter 1 or 2: ")
    
    if mode == "1":
        print(computer_vs_player())
    elif mode == "2":
        print(computer_vs_computer())
    else:
        print("Invalid mode selected. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
