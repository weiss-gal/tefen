import random
import time

games_played = 0
games_human_won = 0
while True:
    choice = None
    print("Welcome to Rock, Paper, Scissors!")
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print("Enter your choice: ")
        choice = input().lower().strip()
        if choice == "rock":
            print("You chose rock!")
        elif choice == "paper":
            print("You chose paper!")
        elif choice == "scissors":
            print("You chose scissors!")
        else:
            print("I don't understand that choice.")
    
    print() # empty line
    for i in range(10):
        print(".", end=" ", flush=True)
        time.sleep(0.5)
    print() # empty line

    machine_choice_int = random.randint(1, 3)
    machine_choice = None
    if machine_choice_int == 1:
        machine_choice = "rock"
    elif machine_choice_int == 2:
        machine_choice = "paper"
    else:    
        machine_choice = "scissors"
    
    print("The machine chose " + machine_choice + "!")

    result_banner = None
    if choice == machine_choice:
        result_banner = "It's a tie!"
    elif choice == "rock" and machine_choice == "scissors" or choice == "paper" and machine_choice == "rock" or choice == "scissors" and machine_choice == "paper":
        result_banner = "You win!"
        games_human_won = games_human_won + 1
    else:
        result_banner = "You lose!"
    
    print() # empty line
    print("*" * (len(result_banner)+4))
    print("* " + result_banner + " *")
    print("*" * (len(result_banner)+4))
    print() # empty line

    games_played = games_played + 1

    print("You have won " + str(games_human_won) + " out of " + str(games_played) + " games.\n")
    print("Play again? (y/n)")
    play_again = input()
    if play_again == "n":
        break