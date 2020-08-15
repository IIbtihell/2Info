import random
import sys

def play():
    while True:
        p_choice = input("What do you choose?")
        cpu_random = random.randint(1,3)
        cpu_choice = cpu_random
if cpu_random == 1:
            cpu_choice = "Rock"
elif cpu_random == 2:
            cpu_choice = "Paper"
elif cpu_random == 3:
            cpu_choice = "Scissors"
def compare():

            play_again = None
if p_choice == cpu_choice:
                print("Tie!")
                play_again = input("Play again?")
elif p_choice == "Rock" and cpu_choice == "Paper":
                print("You Lose!")
                play_again = input("Play again?")
elif p_choice == "Rock" and cpu_choice == "Scissors":
                print("You Win!")
                play_again = input("Play again?")
elif p_choice == "Paper" and cpu_choice == "Scissors":
                print("You Lose!")
                play_again = input("Play again?")
elif p_choice == "Paper" and cpu_choice == "Rock":
                print("You Win!")
                play_again = input("Play again?")
elif p_choice == "Scissors" and cpu_choice == "Rock":
                print("You Lose!")
                play_again = input("Play again?")
elif p_choice == "Scissors" and cpu_choice == "Paper":
                print("You Win!")
                play_again = input("Play again?")
if play_again == "Yes":
                play()
elif play_again == "No":
                print("Game Over")
                sys.exit()
else:
                print("Please try again")
                play_again = input("play again?")
return play_again
def game_start():
    while True:
        begin = input("Would you like to play Rock, Paper, Scissors?")
        if begin == "Yes":
            play()
        return begin
        while begin != "Yes":
          if begin == "No":
                print("Game Over")
                return begin
          else:
                print("Please try again")
                break



