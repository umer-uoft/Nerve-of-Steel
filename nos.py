import time # The time library has a sleep function that will pause the script for a specified amount of time
import random # The random library has a feature that randomly chooses numbers from a range, or a name from the list of players participating in the game.

#program displays "players stand!"
print("Players, please stand!")

#timer is set randomly to anything in between 5-25 seconds.
timer_random = random.choice(range(5,25))
time.sleep(timer_random)

#once the time runs out, the text below is shown.
print('Times up! Last to sit down wins.')

#list of participating players is setup, and a random player is chosen to be the winner.
playerlist = ["Emma", "Fatima", "John", "Bob", "Umer"]
winner = random.choice(playerlist)
print('The winner is', winner + '!')


