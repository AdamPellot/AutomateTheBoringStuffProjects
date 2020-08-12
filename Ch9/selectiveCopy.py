#! python3
# selectiveCopy.py - Walks through a folder tree and searches for files
#                    with a certain file extension. Copy these files
#                    from whatever location they are in to a new folder.
# Adam Pellot

import os
import shutil

print('Enter the path of the folder you would like to use:')
folder = input()

print('Enter the file extension you would like to search for:')
extension = input()

# Create new folder to put these files.
print('Enter the path for a new folder:')
folderPath = input()

# If the folder already exists, move on.
try:
    os.makedirs(folderPath)
except FileExistsError:
    pass


# Walk the entire folder tree and compress the files in each folder.
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith(extension):
            filePath = os.path.join(foldername, filename)
            shutil.copy(filePath, folderPath)
