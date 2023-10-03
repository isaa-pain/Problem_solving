#Description:
#1-Write a Python program that simulates the "Rock, Paper, Scissors" game.
#2-The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").
#3-The player should play against the computer, which will select a random option.
#3-The computer's selection will be compared against the player's selection to determine who wins.
#A descriptive message should be displayed indicating if the player won, lost, or if the game ended in a tie.
#To learn more about this game before starting to solve this challenge, I recommend reading this resource.
#Basic Game Rules:
#Paper beats Rock
#Rock beats Scissors
#Scissors beat Paper.
import random
print("******************************************************")
print("Rock Paper Scissors !")
print("******************************************************")
player_move=input("Type in your choice: ").lower()
computer_move=random.choice(['rock','paper','scissors'])
if (player_move=='scissors' and computer_move=='paper') or (player_move=='paper' and computer_move=='rock') or (player_move=='rock' and computer_move=='scissors'):
    print(f"{player_move} {computer_move} you Won!".format(player_move=player_move,computer_move=computer_move))
elif player_move==computer_move:
    print(f"{player_move} {computer_move} Draw!".format(player_move=player_move,computer_move=computer_move))
else:
    print(f"{player_move} {computer_move} you Lost!".format(player_move=player_move,computer_move=computer_move))
