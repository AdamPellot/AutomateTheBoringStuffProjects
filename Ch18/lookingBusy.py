#! python3
# lookingBusy.py - Nudges the mouse cursor slightly every ten seconds.
# Adam Pellot

import pyautogui
import time


def lookingBusy():
    while True:
        # Nudges the mouse cursor every minute
        pyautogui.moveRel(0, 15, duration=0.25)
        pyautogui.moveRel(0, -15, duration=0.25)
        time.sleep(5)

print('Starting script....')
print('Press CTRl+C to exit.')
try:
    lookingBusy()

except:
    print('Ending script, goodbye.')
