#! python3
# pdfParanoia1.py - Go through every PDF in a folder (and its subfolders)
#                  and encrypt the PDFs using a password provided on the
#                  command line. Save each encrypted PDF with
#                  an _encrypted.pdf suffix added to the original
#                  filename. Before deleting the original file, have the
#                  program attempt to read and decrypt the file to
#                  ensure that it was encrypted correctly.
# Adam Pellot

import os
import PyPDF2
import sys

print('Enter the absolute path of the directory you would like to use:')
folder = input()
os.chdir(folder)
password = sys.argv[1]

# Walk the entire folder tree and compress the files in each folder.
for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        filePath = os.path.join(foldername, filename)
        if filePath.endswith('.pdf'):
            pdfFile = open(filePath, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            newFile = filePath[:-4] + '_encrypted.pdf'
            pdfWriter.encrypt(password)
            resultPdf = open(newFile, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            pdfFile.close()
            # Read and try to decrypt.
            pdfFile = open(newFile, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.isEncrypted is False:
                print(newFile + ' was not encrypted correctly. Try again.')
                break
            if pdfReader.decrypt(password) != 1:
                print(newFile + ' was not encrypted correctly. Try again.')
            pdfFile.close()

# Walk the entire folder tree and deletes the old files without encryption.
for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        filePath = os.path.join(foldername, filename)
        if filePath.endswith('.pdf'):
            if '_encrypted.pdf' not in filename:
                os.unlink(filePath)
