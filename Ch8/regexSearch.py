#! python3
# regexSearch.py - Opens all .txt files in a folder and searches for any
#                  line that matches a user-supplied regular expression.
# Adam Pellot

import os
import re

# Folder path
print('Enter the path of the folder containing the txt files:')
folderPath = input()

# Create the regex the program will search for.
searchRegex = re.compile(r'Hello')

# Loop through every file in the folder and if it ends in .txt, search
# for the regex parrtern in those files.
for file in os.listdir(folderPath):
    if file.endswith('.txt'):
        currentFile = open(os.path.join(folderPath, file))
        lineCount = 1
        for line in currentFile.readlines():
            if searchRegex.findall(line):
                # Print the results if there is a match.
                print(str(searchRegex.findall(line)) + 'found in ' +
                      file + ' on line ' + str(lineCount))
                lineCount += 1
            else:
                lineCount += 1
        currentFile.close()
