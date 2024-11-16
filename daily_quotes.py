# daily_quotes.py

import random

quotes = ["Keep going!", "Believe in yourself!", "You can do it!"]

def get_daily_quote():
    return random.choice(quotes)

# Sample usage
print("Quote of the day:", get_daily_quote())
