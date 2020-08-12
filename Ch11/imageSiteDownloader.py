#! python3
# imageSiteDownloader.py - Takes a category that is inputed by the user
#                          and downloads imgur images of this category
#                          to a folder created by the program.
# Adam Pellot

import requests
import os
import bs4

# Asks for category of pictures.
print('Enter what kind of pictures would you like to download.')
category = input()
url = 'https://imgur.com/search?q=' + category     # Starting url.

os.chdir('C:\\Users\\Adam\\Downloads')

# Store imgur images in ./category_images.
os.makedirs(category + '_images', exist_ok=True)

# Download the page.
print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find the list of images for given category.
images = soup.select('.image-list-link > img')
if images == []:
    print('Could not find images.')
else:
    # Download each image.
    for link in range(len(images)):
        imageSource = 'http://' + images[link].get("src")[2:]
        res = requests.get(imageSource)
        res.raise_for_status()
    # Save each image to ./'category'.
        imageFile = open(os.path.join(category + '_images',
                                      os.path.basename(imageSource)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
            imageFile.close()

print('Done.')
