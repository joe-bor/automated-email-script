import requests
from pprint import pprint

quotes = requests.get('https://zenquotes.io/api/quotes/keyword=success,happiness').json()

# pprint(quotes)