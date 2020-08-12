#! python3
# autoUnsub.py - Scans through your email account, finds all the
#                unsubscribe links in all your emails, and automatically
#                opens them in a browser.
# Adam Pellot

import bs4
import imapclient
import pyzmail
import webbrowser

print('Enter your email address:')
myEmail = input()
print('Enter the password to your email address:')
emailPass = input()

# Connect to email.
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(myEmail, emailPass)
imapObj.select_folder('INBOX', readonly=True)

# Select all emails and check for each one unsub link.
UIDs = imapObj.search('ALL')
unsubLinks = []
count = 0
for ID in UIDs:
    rawMessages = imapObj.fetch(ID, ['BODY[]'])
    message = pyzmail.PyzMessage.factory(rawMessages[ID][b'BODY[]'])
    if message.html_part:
        htl = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(htl, 'html.parser')
        linkElems = soup.select('a')
        for link in linkElems:
            if 'unsubscribe' in link.text.lower():
                unsubLinks.append(link.get('href'))
imapObj.logout()

# Open each unsub link in webbrowser.
for link in unsubLinks:
    webbrowser.open(link)
