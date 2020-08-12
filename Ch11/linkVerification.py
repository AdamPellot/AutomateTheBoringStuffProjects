#! python3
# linkVerification.py - Given a url from command line args, attempt to
#                       download from every link using bs4 and report
#                       the status.
# Adam Pellot

import bs4
import requests
import re

# Download the page.
# url = sys.argv[1]
url = 'https://automatetheboringstuff.com'
print('Downloading page %s...' % url)
res = requests.get(url)
try:
    res.raise_for_status()
except:
    print('The website you are trying to access is a broken link')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Download from all urls on the page.
count = 1
for link in soup.find_all("a"):
    if link is None:
        link = link.get("name")
        print(link)
    else:
        link = link.get("href")
    print('CHECKING THE STATUS OF LINK #' + str(count) + ': ' + link)
    count = count + 1
    res = requests.get(link)
    try:
        res.raise_for_status()

    except Exception as e:
        if res.status_code == 404:
            print('THIS IS A BROKEN LINK: ' + print(str(e)))
            print('')
        else:
            print(str(e))
            print('')

print('Done.')
