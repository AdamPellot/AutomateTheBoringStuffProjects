#! python3
# commandLineEmailer - Uses selenium module to log into the users yahoo
#                      email account and send an email using command
#                      line arguments. sys.argv[1] is the email of the
#                      recipient and while sys.argv[2:] is the message
#                      you would like to send.
# Adam Pellot

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Joins the command line arguments by a space to create the message that will
# be sent in the email.
message = ' '.join(sys.argv[2:])

# Opens controlled Firefox broswer.
browser = webdriver.Firefox()
browser.get('''https://login.yahoo.com/?.src=ym&.lang=en-US&.intl=us&.
done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.intl%3Dus''')

# Logs into email.
emailElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "login-username")))
emailElem.send_keys('email username')
linkElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-signin")))
linkElem.click()
passwordElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input#login-passwd")))
passwordElem.send_keys('email pass')
linkElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-signin")))
linkElem.click()
linkElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.e_dRA")))
linkElem.click()

# Composes and sends message.
toElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#message-to-field")))
toElem.send_keys(sys.argv[1])

subjectElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input.q_T:nth-child(1)")))

# Subject text.
subjectElem.send_keys("This message was sent from Adam's PC")

# Type message.
textElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-test-id = "rte"]')))
textElem.send_keys(message)

# Send email.
sendElem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.q_Z2aVTcY')))
sendElem.click()
