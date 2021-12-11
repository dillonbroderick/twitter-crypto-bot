from bs4 import BeautifulSoup
import requests
import time
import tweepy
from datetime import datetime

API_KEY = 'mbYvbcFKldkdBnzE0wdgvoAhb'
API_SECRET_KEY = 'S9qUvNGNGbkaj8mOBwi8kIm3t8u0tWUYgkA35sGVXpeXVeM63f'

ACCESS_TOKEN = '1468008570146865152-vW3SFHQOLa3weqNTyzSOJtnVWEV0i3'
ACCESS_TOKEN_SECRET = '9t3ttK7lCm9TtVnHs9cGDsBLjcbS8VTXDc25eNszF46zx'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def getPrice(coin):
    # Get the URL
    url = "https://www.google.com/search?q=" + coin + "+price"

    # Make a request to the website
    HTML = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')

    # Find the current price
    # text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find("div",attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

def getPercentageChange(prevPrice, currPrice):
    if (prevPrice > currPrice):
        return round((-1 * (prevPrice/currPrice)), 2)
    elif (prevPrice == currPrice):
        return 0.00
    else:
        return round(currPrice / prevPrice, 2)

PREV_ETHEREUM_PRICE = 4003.51
PREV_BITCOIN_PRICE = 48260.20
PREV_CARDANO_PRICE = 1.23

while True:
    now = datetime.now()
    formattedDateTime = now.strftime("%m/%d/%Y %H:%M:%S")

    ETHEREUM_UNFIXED_PRICE = getPrice("ethereum")
    BITCOIN_UNFIXED_PRICE = getPrice("bitcoin")
    CARDANO_UNFIXED_PRICE = getPrice("cardano")

    ETHEREUM_PRICE = ETHEREUM_UNFIXED_PRICE[0 : len(ETHEREUM_UNFIXED_PRICE) - 21]
    BITCOIN_PRICE = BITCOIN_UNFIXED_PRICE[0 : len(BITCOIN_UNFIXED_PRICE) - 21]
    CARDANO_PRICE = CARDANO_UNFIXED_PRICE[0 : len(CARDANO_UNFIXED_PRICE) - 21]

    api.update_status(
        formattedDateTime
        + "\nBTC price: $" + str(BITCOIN_PRICE)
        + "\nBTC percentage change: " + str(getPercentageChange(PREV_BITCOIN_PRICE, float(BITCOIN_PRICE.replace(',', '')))) + "%"
        + "\nETH price: $" + str(ETHEREUM_PRICE)
        + "\nETH percentage change: " + str(getPercentageChange(PREV_ETHEREUM_PRICE, float(ETHEREUM_PRICE.replace(',', '')))) + "%"
        + "\nCRD price: $" + str(CARDANO_PRICE)
        + "\nCRD percentage change: " + str(getPercentageChange(PREV_CARDANO_PRICE, float(CARDANO_PRICE.replace(',', '')))) + "%")

    PREV_ETHEREUM_PRICE = float(ETHEREUM_PRICE.replace(',', ''))
    PREV_BITCOIN_PRICE = float(BITCOIN_PRICE.replace(',', ''))
    PREV_CARDANO_PRICE = float(CARDANO_PRICE.replace(',', ''))
    time.sleep(86400)





