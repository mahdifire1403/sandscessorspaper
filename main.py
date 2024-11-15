import random
print("Rock".lower())
print("Paper".lower())
print("Scissors".lower())
print("__________________________")
# set random
random_Number = random.randint(0, 2)
# set moves for computer
if random_Number == 0:
    computer_Move = "rock"
if random_Number == 1:
    computer_Move = "paper"
if random_Number == 2:
    computer_Move = "scissors"
    # print("compute_Move")
    # set player1
    player_1 = input("player_1, make your move:")
    # set player2
    player_2 = computer_Move
    print(f"player_2, make your move: {computer_Move}")
# set rules of players
    if player_1 == player_2:
        print("that is a tie")
    elif player_1 == "rock":
        if player_2 == "scissors":
            print("player_1 wins... ")
        elif player_2 == "paper":
            print("player_2 wins...")
        elif player_1 == "paper":
            if player_2 == "rock":
                print("player_2 wins...")
            elif player_2 == "scissors":
                print("player_2 wins...")
    else:
        print("something went wrong")
