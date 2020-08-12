#! python3
# discordIMBot.py - Automatically send out a notification message to a
#                   select group of people on your friend list in
#                   discord.
# Adam Pellot

import pyautogui
import time

print('Enter the message you would like to send to your friends:')
message = input()

print('Enter the names of your friends on discord separated by a comma')
friends = input()

friendsList = friends.split(",")

# Locate home button in discord.
discordHome = pyautogui.locateCenterOnScreen(
    'C:\\Users\\Adam\\Pictures\\discordHome.png')

# If home is already selected located selected home icon.
if discordHome is None:
    discordHome = pyautogui.locateCenterOnScreen(
        'C:\\Users\\Adam\\Pictures\\discordSelectedHome.png')

# Click on home on discord
pyautogui.click(discordHome[0], discordHome[1])

time.sleep(3)

# Locate the create DM button on discord.
createDM = pyautogui.locateCenterOnScreen(
    'C:\\Users\\Adam\\Pictures\\discordCreateDM.png')

time.sleep(3)

# Click on the create DM button on discord.
pyautogui.click(createDM[0], createDM[1])

# Add friends to the group DM on discord.
for person in friendsList:
    person = person.lstrip()
    pyautogui.typewrite(person)
    pyautogui.press('enter')

# Locate create group DM button on discord.
createGroupDM = pyautogui.locateCenterOnScreen(
    'C:\\Users\\Adam\\Pictures\\discordCreateGroupDM.png')
# Click on the create group DM button on discord.
pyautogui.click(createGroupDM[0], createGroupDM[1])

pyautogui.typewrite(message)
pyautogui.press('enter')
