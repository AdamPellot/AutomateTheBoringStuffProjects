#! python3
# randChoreAssgn.py - Takes a list of people’s email addresses and a
#                     list of chores that need to be done and randomly
#                     assigns chores to people.
# Adam Pellot

import ezgmail
import os
import random
import shelve

# Change directory to the one containing the token.json
# and credentials.json for ezgmail.
os.chdir('C:\\Users\\Adam\\Downloads')

# List of recipients.
recipients = ['example1@gmail.com', 'example2@gmail.com',
              'example3@gmail.com', 'example4@gmail.com']

# Open Chores shelf.
lastChoreShelf = shelve.open('chores')

# Setup last chore shelf if the shelf is empty.
if len(lastChoreShelf) == 0:
    for recipient in recipients:
        lastChoreShelf[recipient] = 'n/a'

    lastChoreShelf['chores'] = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# Give each recipient a chore that was different from their last one.
chores = lastChoreShelf['chores']
for recipient in recipients:
    assignedChore = random.choice(chores)
    lastChore = lastChoreShelf[recipient]
    if assignedChore == lastChore:
        while assignedChore == lastChore:
            assignedChore = random.choice(chores)
    lastChoreShelf[recipient] = assignedChore
    chores.remove(assignedChore)

# Send chores.
for recipient in recipients:
    ezgmail.send(recipient, 'Your chore for the week',
                 'Your chore for this week is: ' + lastChoreShelf[recipient])

# Close shelf.
lastChoreShelf.close()
