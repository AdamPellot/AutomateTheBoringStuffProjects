#! python3
# fillTheGaps.py - Finds all files with a given prefix, such as
#                  spam001.txt, spam002.txt, and so on, in a single
#                  folder and locates any gaps in the numbering. Have
#                  the program rename all the later files to close this
#                  gap.
# Adam Pellot

import re
import os
import shutil


# Returns boolean based on if the passed string has a file extension.
def isFileExtension(filename):
    extensionRegex = re.compile(r'\.[a-zA-Z]{3,4}')
    mo = extensionRegex.search(filename)
    if not mo:
        return True
    else:
        return False

print('Enter the absolute path of the folder you want to search:')
folder = input()

print('''Enter the name of the file without the desired prefix:
(Ex. Enter spam.txt instead of spam001.txt)''')
filename = input()
if isFileExtension(filename) is False:
    while isFileExtension(filename) is False:
        print('Invalid filename: File extension not found')
        print('''Enter the name of the file without the desired prefix:
(Ex. Enter spam.txt instead of spam001.txt)''')
        filename = input()

print('''Finally enter the prefix you would like to use starting at 1:
(Ex. 001, 01, 1)''')
prefix = input()

# Ensures extension starts at 1.
if prefix[-1] != '1':
    while True:
        print('Invalid Prefix')
        print('''Please enter the prefix that starts at 1:
(Ex. 001, 01, 1)''')
        extension = input()
        if prefix[-1] == '1':
            break

# If the prefix is something like 001, this holds those 0's.
charsBeforeNum = prefix[:-1]

# Create variable that holds the file extension.
extensionRegex = re.compile(r'\.[a-zA-Z]{3,4}')
mo = extensionRegex.search(filename)
extension = mo.group()

# Holds a string of the file without extension. So is spam.txt is spam.
filewoExtension = filename.replace(extension, '')

# Create regex that detects the file number.
fileNumRegex = re.compile(r'([1-9]+[0]*)\.')

fileNums = []

# Put the file numbers in a list.
for file in os.listdir(folder):
    if filewoExtension in file:
        mo = fileNumRegex.search(file)
        fileNums.append(int(mo.group(1)))

# Sort the list of file numbers.
fileNums.sort()

# Determines where the gap in the numbering begins
for i in range(len(fileNums)):
    if fileNums[i] + 1 != fileNums[i+1]:
        gapStart = fileNums[i]
        break

filesToBeRenamed = []
# Determines which numbered files have to be renamed to keep the numbering.
for file in os.listdir(folder):
    if filewoExtension in file:
        mo = fileNumRegex.search(file)
        if int(mo.group(1)) > gapStart:
            filesToBeRenamed.append(int(mo.group(1)))

# Sort the list of file numbers to be renamed.
filesToBeRenamed.sort()

newFileNum = gapStart + 1
# Fills in the gaps in the numbering.
for i in range(len(filesToBeRenamed)):
    filePath = os.path.join(folder, filewoExtension + charsBeforeNum +
                            str(filesToBeRenamed[i]) + extension)
    newFilePath = os.path.join(folder, filewoExtension + charsBeforeNum +
                               str(newFileNum) + extension)
    newFileNum += 1
    if os.path.exists(filePath):
        os.rename(filePath, newFilePath)
