#! python3
# txt2Sheet.py - Read in the contents of several text files and insert
#                those contents into a spreadsheet, with one line of
#                text per row.
# Adam Pellot

import os
import openpyxl

# Directory with the txt files.
os.chdir('C:\\Users\\Adam\\Documents')

# Create a new workbook.
wb = openpyxl.Workbook()
sheet = wb['Sheet']

# Open the txt files and put their contents in a spreadsheet.
print('How many text files will you be using today?')
n = int(input())

print('Creating spreadsheet....')
for files in range(n):
    print('Enter the name of file #' + str(files + 1) + '.')
    filename = input()
    file = open(filename)
    contents = []
    for line in file.readlines():
        contents.append(line)
    for rowNum in range(len(contents)):
        sheet.cell(row=rowNum + 1, column=files + 1).value = contents[rowNum]
# Save the new workbook and close the files.
wb.save('newSpreadSheet.xlsx')
wb.close()

print('Done.')
