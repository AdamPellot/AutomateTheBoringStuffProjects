#! python3
# pdfParanoia2.py - Finds all encrypted PDFs in a folder (and its
#                   subfolders) and creates a decrypted copy of the PDF
#                   using a provided password. If the password is
#                   incorrect, the program should print a message to the
#                   user and continue to the next PDF.
# Adam Pellot

import os
import PyPDF2
import sys

print('Enter the absolute path of the directory you would like to use:')
folder = input()

password = sys.argv[1]

# Walk the entire folder tree and compress the files in each folder.
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        filePath = os.path.join(foldername, filename)
        if filePath.endswith('_encrypted.pdf'):
            pdfFile = open(filePath, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.decrypt(password) != 1:
                print('The given password is not correct for.' + filename)
                print('Moving on to next file.')
                continue
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            newFile = filePath[:-14] + '.pdf'
            resultPdf = open(newFile, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            pdfFile.close()
