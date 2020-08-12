#! python3
# customSeatingInvite.py - Generates seating invitations.
# Adam Pellot

import os
from PIL import Image, ImageDraw, ImageFont

# Flower image used to decorate card.
flower = Image.open('flower.png')

# Directory to store seating invitations.
os.makedirs('seatingCards', exist_ok=True)

print('Enter the absolute path of the file with your guest list')
guestsPath = input()
guestsFile = open(guestsPath)

for name in guestsFile.readlines():
    name = name.rstrip('\n')
    # Create the card.
    card = Image.new('RGBA', (360, 288), 'white')
    card.paste(flower, (0, 0))

    # Create the border.
    guideLine = Image.new('RGBA', (368, 296), 'black')

    # Add the border onto the card.
    guideLine.paste(card, (4, 4))

    # Add name onto the card.
    guestName = ImageDraw.Draw(guideLine)
    fontFolder = 'C:\\Users\\Adam\\Documents\\fontFolder'
    cardFont = ImageFont.truetype(os.path.join(fontFolder,
                                  'Arial.ttf'), 46)
    guestName.text((120, 100), name, fill='black', font=cardFont)

    # Save card
    fileName = name + '_Invite.png'
    guideLine.save(fileName)
