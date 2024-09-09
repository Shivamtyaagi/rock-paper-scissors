import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

User_Name = input("Player Name : ")
print("Welcome to rock, paper scissors game and your opponent is Computer")


while True:
    user_input = input("Enter rock/paper/scissors or q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_picked = options[random_number]
    print("Computer picked", computer_picked + ".")


    if user_input == computer_picked:
        print("Match Draw")
        
    elif user_input == "rock" and computer_picked == "scissors":
        print("you won!!")
        user_win+=1
    
    elif user_input == "scissors" and computer_picked == "paper":
        print("you won!!")
        user_win+=1

    elif user_input == "paper" and computer_picked == "rock":
        print("you won!!")
        user_win+=1

    else:
        print("You lost!!")
        computer_win+=1


print(User_Name, "won", user_win, "times")
print("computer won", computer_win, "times") 
print("Good Bye!!, Thanks for playing")

