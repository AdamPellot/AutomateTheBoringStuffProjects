#! python3
# umbrellaReminder.py - Checks whether it’s raining today. If so, have
#                       the program text you a reminder to pack an
#                       umbrella before leaving the house.
# Adam Pellot


import bs4
import requests
from twilio.rest import Client

# Twilio account information.
accountSID = 'Enter Information'
authToken = 'Enter Information'
myCellPhone = 'Enter Information'
myTwilioNumber = 'Enter Information'
twilioCli = Client(accountSID, authToken)

forecastWebsite = '''https://forecast.weather.gov/MapClick.php
                  ?lat=28.90769000000006&lon=-81.18443999999994'''

# Download weather.gov site with today's forecast.
res = requests.get(forecastWebsite)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Scans today's forecast element on weather.gov.
todayForecastElem = soup.select('div.row-odd:nth-child(1) > div:nth-child(2)')
forecast = todayForecastElem[0].getText()

# Sends text message.
if 'showers' in forecast.lower():
    twilioCli.messages.create(body='You need to bring an umbrella today.',
                              from_=myTwilioNumber, to=myCellPhone)
else:
    twilioCli.messages.create(body='No umbrella today.',
                              from_=myTwilioNumber, to=myCellPhone)
