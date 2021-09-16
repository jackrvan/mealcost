#!/usr/bin/env python

import requests
import re
from bs4 import BeautifulSoup

fractions = {
    0x2189: '0.0',  # ; ; 0 # No       VULGAR FRACTION ZERO THIRDS
    0x2152: '0.1',  # ; ; 1/10 # No       VULGAR FRACTION ONE TENTH
    0x2151: '0.11111111',  # ; ; 1/9 # No       VULGAR FRACTION ONE NINTH
    0x215B: '0.125',  # ; ; 1/8 # No       VULGAR FRACTION ONE EIGHTH
    0x2150: '0.14285714',  # ; ; 1/7 # No       VULGAR FRACTION ONE SEVENTH
    0x2159: '0.16666667',  # ; ; 1/6 # No       VULGAR FRACTION ONE SIXTH
    0x2155: '0.2',  # ; ; 1/5 # No       VULGAR FRACTION ONE FIFTH
    0x00BC: '0.25',  # ; ; 1/4 # No       VULGAR FRACTION ONE QUARTER
    0x2153: '0.33333333',  # ; ; 1/3 # No       VULGAR FRACTION ONE THIRD
    0x215C: '0.375',  # ; ; 3/8 # No       VULGAR FRACTION THREE EIGHTHS
    0x2156: '0.4',  # ; ; 2/5 # No       VULGAR FRACTION TWO FIFTHS
    0x00BD: '0.5',  # ; ; 1/2 # No       VULGAR FRACTION ONE HALF
    0x2157: '0.6',  # ; ; 3/5 # No       VULGAR FRACTION THREE FIFTHS
    0x215D: '0.625',  # ; ; 5/8 # No       VULGAR FRACTION FIVE EIGHTHS
    0x2154: '0.66666667',  # ; ; 2/3 # No       VULGAR FRACTION TWO THIRDS
    0x00BE: '0.75',  # ; ; 3/4 # No       VULGAR FRACTION THREE QUARTERS
    0x2158: '0.8',  # ; ; 4/5 # No       VULGAR FRACTION FOUR FIFTHS
    0x215A: '0.83333333',  # ; ; 5/6 # No       VULGAR FRACTION FIVE SIXTHS
    0x215E: '0.875',  # ; ; 7/8 # No       VULGAR FRACTION SEVEN EIGHTHS
}

def replace_fractions(text):
    """replace_fractions. This function is a bloody mess. Should find a simpler way to do this. Big Yikes
        Would probably be better as a module.

    Args:
        text: The text you want to replace the fractions in.
    """
    split_text = text.split(' ')
    try:
        if ord(split_text[0][0]) in fractions:
            # Text starts with a fraction. Simply replace the fraction and return it
            pattern = re.compile('|'.join([chr(x) for x in fractions.keys()]))
            return pattern.sub(lambda x: fractions[ord(x.group())], text)
        elif ord(split_text[1][0]) in fractions:
            # Text starts with a whole number and then a fraction. 1 1/2
            pattern = re.compile('|'.join([chr(x) for x in fractions.keys()]))
            new_string = pattern.sub(lambda x: fractions[ord(x.group())], text)
            return str(float(new_string.split(' ')[0]) + float(new_string.split(' ')[1])) + ' ' + ' '.join(new_string.split(' ')[2:])
    except IndexError:
        # Just means first item is empty. Happens sometimes.
        return text
    return text

url = 'https://www.allrecipes.com/recipe/261544/juicy-honey-fried-chicken/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
ingredients = [replace_fractions(x.string.replace('\u2009', ' '))
                    for x in soup.find_all(class_='ingredients-item-name')]
for ingredient in ingredients:
    print(f"{ingredient=}")
