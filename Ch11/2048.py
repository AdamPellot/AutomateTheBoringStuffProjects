#! python3
# 2048.py - Uses selenium module to open a game of 2048 and repeatedly
#           enter the up right down left key strokes to obtain a high
#           score.
# Adam Pellot

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Opens controlled Firefox broswer and loads 2048 game.
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
gameElem = browser.find_element_by_tag_name('html')

# Enters key strokes until no more moves can be made.
while True:
    gameElem.send_keys(Keys.UP)
    gameElem.send_keys(Keys.RIGHT)
    gameElem.send_keys(Keys.DOWN)
    gameElem.send_keys(Keys.LEFT)
