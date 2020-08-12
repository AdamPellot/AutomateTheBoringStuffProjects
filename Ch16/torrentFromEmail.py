#! python3
# torrentFromEmail.py - Checks your email account every 15 minutes for any
#                       magnet links you email it and downloads the content
#                       automatically through qBittorrent.
# Adam Pellot

import imapclient
import pyzmail
import subprocess
import time
from twilio.rest import Client

# Enter Twilio account information.
accountSID = 'Enter Information'
authToken = 'Enter Information'
myCellPhone = 'Enter Information'
myTwilioNumber = 'Enter Information'
twilioCli = Client(accountSID, authToken)


def checkEmail():
    # Will not follow instructions unless verification pass is present
    # in the email.
    verifPass = 'Enter Information'
    myEmail = 'Enter Information'
    emailPass = 'Enter Information'

    # Connect to email.
    twilioCli.messages.create(body='Connecting to email.',
                              from_=myTwilioNumber, to=myCellPhone)
    time.sleep(4)
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login(myEmail, emailPass)
    imapObj.select_folder('INBOX', readonly=False)

    # Select all emails and check each one for unsub link.
    twilioCli.messages.create(body='Searching email.',
                              from_=myTwilioNumber, to=myCellPhone)
    time.sleep(4)
    UIDs = imapObj.search('FROM ' + myEmail)
    links = []
    for ID in UIDs:
        rawMessages = imapObj.fetch(ID, ['BODY[]'])
        message = pyzmail.PyzMessage.factory(rawMessages[ID][b'BODY[]'])
        textPart = message.text_part
        # If the verification password is in the email get the link.
        if verifPass in textPart.get_payload().decode(textPart.charset):
            print('hi')
            text = textPart.get_payload().decode(textPart.charset)
            # Finds magnet link in body of email.
            linkIndex = text.find('magnet')
            link = text[linkIndex:]
            links.append(link)
            imapObj.delete_messages(ID)
            imapObj.expunge()

    imapObj.logout()

    if len(links) == 0:
        twilioCli.messages.create(body='No magnets found.',
                                  from_=myTwilioNumber, to=myCellPhone)
        return
    # Run qBittorrent.
    twilioCli.messages.create(body='Opening qBittorrent.',
                              from_=myTwilioNumber, to=myCellPhone)
    qbProcess = subprocess.Popen(['D:\\qBittorrent\\qbittorrent.exe', link])
    qbProcess.wait()

while True:
    twilioCli.messages.create(body='Starting Program.',
                              from_=myTwilioNumber, to=myCellPhone)
    time.sleep(4)
    checkEmail()
    time.sleep(60 * 15)
