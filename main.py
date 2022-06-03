#THIS IS THE MAIN SOLUTION
#THIS IS THE MAIN SOLUTION
#THIS IS THE MAIN SOLUTION
#THIS IS THE MAIN SOLUTION


import random

def play():
    user_choice = input("Choose Rock, Paper or Scissors:")
    if user_choice in ["rock", "r", "R",]:
        user_choice = "r"
    elif user_choice in ["paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("Error!!! Try again.")
        play()
    return user_choice    

computer = random.choice(["r", "p", "s"])

while True:
    print("")
    user_choice = play()
    computer = random.choice(["r", "p", "s"])
    print("")
   # if user_choice == computer:
       # return "You and computer have both chosen {}.It's a Tie".format(computer)

    if user_choice == "r":
        if computer == "r":
            print("You picked rock. Computer picked rock. It's a Tie!!")
        elif computer == "p":
            print("You picked rock. Computer picked paper. You Lost!!")
        elif computer == "s":
            print("You picked rock. Computer picked scissors. You Win!!")

    elif user_choice == "p":
        if computer == "r":
            print("You picked paper. Computer picked rock. You Win!!")
        elif computer == "p":
            print("You picked paper. Computer picked paper. It's a Tie!!")
        elif computer == "s":
            print("You picked paper. Computer picked scissors. You Lost!!")

    elif user_choice == "s":
        if computer == "r":
            print("You picked scissors. Computer picked rock. You Lost!!")
        elif computer == "p":
            print("You picked scissors. Computer picked paper. You Win!!")
        elif computer == "s":
            print("You picked scissors. Computer picked scissors. It's a Tie!!")

            print("")            

# THANK YOU
# THANK YOU
# THANK YOU


