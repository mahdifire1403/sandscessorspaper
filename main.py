import random
random_Number = random.randint(0,2)
if random_Number == 0:
    computer_Move = "rock"
if random_Number == 1:
    computer_Move = "paper"
if random_Number == 2:
    computer_Move = "scissors"
    print("compute_Move")
    player_1 = input(f"player_1: make your move,{computer_Move}")
    player_2 = input("player_1:make your move")
