#! python3
# passBreak.py - Decrypts the PDF by trying every possible English word
#                until it finds one that works.
# Adam Pellot

import PyPDF2

print('Enter the absolute path of the pdf you would like to decrypt:')
file = input()

print('Enter the absolute path of the dictionary file:')
dictPath = input()

# Open dictionary.
dictionary = open(dictPath)

# Open pdf and compare password to dict entries.
matchFound = 0
pdfFile = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
for word in dictionary.readlines():
    word = word.strip('\n')
    print(word)
    if pdfReader.decrypt(word) == 1:
        print('File successfully decrypted,')
        print('The password is "' + word + '"')
        matchFound = 1
        break
    if pdfReader.decrypt(word.lower()) == 1:
        print('File successfully decrypted,')
        print('The password is "' + word.lower() + '"')
        matchFound = 1
        break
    if pdfReader.decrypt(word.lower().capitalize()) == 1:
        print('File successfully decrypted,')
        print('The password is "' + word.lower().capitalize + '"')
        matchFound = 1
        break
if matchFound == 1:
    pass
else:
    print('No matches found, unable to decrypt file')
pdfFile.close()
