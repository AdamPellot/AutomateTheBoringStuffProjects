#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword.
#        py.exe mcb.pyw deleteAll - Deletes all keywords.
# Adam Pellot

import shelve
import pyperclip
import sys


mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# Delete keywords.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
if len(sys.argv) == 2 and sys.argv[1] == 'deleteAll':
    for keys in list(mcbShelf.keys()):
            del mcbShelf[keys]
    
# List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    else:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
