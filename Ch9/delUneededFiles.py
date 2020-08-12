#! python3
# delUneededFiles.py - Walks through a folder tree and searches for
#                      exceptionally large files or folders—say, ones
#                      that have a file size of more than 100MB. Print
#                      these files with their absolute path to the
#                      screen.
# Adam Pellot

import os
import shutil

print('Enter the path of the folder you would like to use:')
folder = input()

# Walk the entire folder tree and search files and folders for large files.
for foldername, subfolders, filenames in os.walk(folder):
    for subfolder in subfolders:
        filePath = os.path.join(foldername, subfolder)
        if os.path.getsize(filePath) > 100000000:
            print(os.path.abspath(subfolder))
    for filename in filenames:
        filePath = os.path.join(foldername, filename)
        if os.path.getsize(filePath) > 100000000:
            print(os.path.abspath(filename))
