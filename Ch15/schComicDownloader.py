#! python3
# schComicDownloader.py - Checks the websites of several web comics and
#                         automatically downloads the images if the
#                         comic was updated since the program’s last
#                         visit.
# Adam Pellot

import bs4
import os
import shelve
import requests


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; \
                   Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}


def downloadXkcd(startingUrl):  # Download from xkcd.com.
    url = startingUrl
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    nextLink = soup.select('a[rel="next"]')[0]
    url = 'http://xkcd.com' + nextLink.get('href')
    if url.endswith('#'):
        print('There are no new comics from XKCD.')
    # Checks for new comics to download after the last comic
    # number recorded.
    while not url.endswith('#'):
        # On the last loop the current comic number will be recorded.
        comicShelf['lastXkcdUrl'] = url

        # Download the page.
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.basename(comicUrl), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        # Get the Next button's url.
        nextLink = soup.select('a[rel="next"]')[0]
        url = 'http://xkcd.com' + nextLink.get('href')


def downloadButter(lastDate):  # Download from buttersafe.com.
    url = 'https://www.buttersafe.com/'
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the date of the most recent comic.
    dateElem = soup.select('#headernav-date')
    date = dateElem[0].text.strip()

    # No new comics have been uploaded.
    if date == lastDate:
        print('There are no new comics from buttersafe.')
    else:
        # Put the new latest date in shelf.
        comicShelf['lastButterDate'] = date
        while date != lastDate:
            print('Downloading page %s...' % url)
            res = requests.get(url, headers=headers)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            # Download the image.
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Could not find comic image.')
            else:
                comicUrl = comicElem[0].get('src')
                print('Downloading image %s...' % (comicUrl))
                res = requests.get(comicUrl, headers=headers)
                res.raise_for_status()

                # Save the image.
                imageFile = open(os.path.basename(comicUrl), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

            # Get the Next button's url and date.
            prevLink = soup.select('a[rel="prev"]')[0]
            url = prevLink.get('href')

            res = requests.get(url, headers=headers)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'html.parser')

            # Find the date of the previous comic.
            dateElem = soup.select('#headernav-date')
            date = dateElem[0].text.strip()

# Create directory to store comics.
os.makedirs('C:\\Users\\Adam\\Desktop\\comics', exist_ok=True)
os.chdir('C:\\Users\\Adam\\Desktop\\comics')

comicShelf = shelve.open('comic')

# First time running program.
if len(comicShelf) == 0:
    comicShelf['lastXkcdUrl'] = 'https://xkcd.com/2248/'
    comicShelf['lastButterDate'] = 'Thursday, December 26th, 2019'
    downloadXkcd(comicShelf['lastXkcdUrl'])
    downloadButter(comicShelf['lastButterDate'])

else:
    downloadXkcd(comicShelf['lastXkcdUrl'])
    downloadButter(comicShelf['lastButterDate'])

comicShelf.close()
