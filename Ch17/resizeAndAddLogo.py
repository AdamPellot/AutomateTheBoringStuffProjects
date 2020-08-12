#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
#                       in a 300x300 square, and adds catlogo.png to the
#                       lower-right corner.
# Adam Pellot

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

filetypes = ['.gif', '.png', '.bmp', '.jpg']

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    name, ext = os.path.splitext(filename.lower())
    if ext not in filetypes:
        continue
    if filename == LOGO_FILENAME:
        continue

    print(filename)
    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add logo when image is at least twice the width and height of the logo.
    if width >= (logoWidth * 2) and height >= (logoHeight * 2):
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    else:
        print('Logo mark skipped, it would take to much space on the image.')
    # Save changes.
    im.save(os.path.join('withLogo', filename))
