import string
from random import choices
def generate_short () :
    symbols = string.digits + string.ascii_letters
    short_url = ''.join(choices(symbols, k = 3))