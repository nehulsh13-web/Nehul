import random
while True:
    user_action = input("Enter a choice(Rock, Paper, Scissors): ")
    possible_action = ["Rock","Paper","Scissors"]
    robot = random.choice(possible_action)
    print(f"\nYou chose {user_action}, and robot chose {robot}\n")
    if user_action == robot:
        print("Its a draw")
    elif user_action == "Rock":
        if robot == "Paper":
            print("Robot has won")
        else:
            print("You have won")
    elif user_action == "Paper":
        if robot == "Scissors":
            print("Robot has won")
        else:
            print("You have won")
    elif user_action == "Scissors":
        if robot == "Rock":
            print ("Robot has won")
        else:
            print("You have won")
    play_again = input("Play Again (Yes/No): ")
    if play_again == "Yes":
        break 
        