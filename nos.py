"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 
import random

#program displays "players stand!"
print("Players, please stand!")

timer_random = random.choice(range(5,25))
time.sleep(timer_random)

print('Times up! Last to sit down wins.')

