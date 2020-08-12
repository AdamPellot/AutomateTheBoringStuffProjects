#! python3
# madLibs.py - Reads in text files and lets the user add their own text
#              anywhere the word ADJECTIVE, NOUN, ADVERB, VERB appears.
# Adam Pellot

import os
import re

print('Enter the directory file you would like to read in:')
directory = input()
os.chdir(directory)

print('Enter the file you would like to read in:')
filename = input()

# Open file thats being read in and create new file.
file = open(filename)
newFile = open('new' + filename, 'a')

# Create list for ADJECTIVE, NOUN, ADVERB, or VERB.
typeRegex = re.compile(r'''ADJECTIVE[ \.\?!,"\']|NOUN[ \.\?!,"\']|
                        ADVERB[ \.\?!,"\']|VERB[ \.\?!,"\']''')

# Create a regex to detect words.
wordRegex = re.compile(r'\w+[\n\.\?!,"\' ]')


# Scan each line word by word and check if each word matches a word type.
for line in file.readlines():
    string = line
    wordList = wordRegex.findall(string)
    typeList = typeRegex.findall(string)
    count = 0
    for word in wordList:
        # If word in the line matches 1 of the 4 types, enter new word.
        if word in typeList:
            print('Enter a ' + word[:-1] + ':')
            newWord = input()
            wordList[count] = newWord + word[-1]
            if '.' in word or ',' in word:
                wordList[count] = wordList[count] + ' '
            count += 1
        else:
            if '.' in word or ',' in word:
                wordList[count] = wordList[count] + ' '
            count += 1
    newFile.write(''.join(wordList))

# Close files.
file.close()
newFile.close()
