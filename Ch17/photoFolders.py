#! python3
# photoFolders.py - Prints the names of folders where more than half
#                   of the files are either a png or jpg.
# Adam Pellot

import os
from PIL import Image

filetypes = ['.png', '.jpg']

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        name, ext = os.path.splitext(filename.lower())
        # Check if file extension isn't .png or .jpg.
        if ext not in filetypes:
            numNonPhotoFiles += 1
            continue    # skip to next filename
        # Open image file using Pillow.
        try:
            im = Image.open(os.path.join(foldername, filename))
        except:
            continue

        width, height = im.size

        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername))
