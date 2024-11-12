import random
random_Number = random.randint(0, 2)
if random_Number == 0:
    computer_Move = "rock"
if random_Number == 1:
    computer_Move = "paper"
if random_Number == 2:
    computer_Move = "scissors"
    print("compute_Move")
    player_1 = input(f"player_1, make your move: {computer_Move}")
    player_2 = input(f"player_2, make your move: {computer_Move}")
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
    else: print("something went wrong")
