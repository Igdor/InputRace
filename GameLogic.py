import urllib
import requests
import re
import logging

from bs4 import BeautifulSoup
from requests_html import HTMLSession


def parser(word):
    """Searches the word in google and returns approximate number of results"""
    query = urllib.parse.quote_plus(word)
    try:
        session = HTMLSession()
        response = session.get("https://www.google.com/search?q=" + query + "&hl=en")
        soup = BeautifulSoup(response.text, 'html.parser')
        stats = soup.find('div', id="result-stats")
        logging.info("Result stats for word " + word + " retrieved: " + str(stats))
        if stats is None:
            logging.warning("bad HTML loaded for word " + word)
            return parser(word)  # searches with requests_html sometimes fail to return number of results, prob because
            # of Google anti-parser measures, so this loop was added as a countermeasure
        word_popularity = re.search("About (.*?) results", stats.text).group(1)
        return int(re.sub(",", "", word_popularity))

    except requests.exceptions.RequestException as e:
        logging.error(e)


def boost_calculator(word, used_words):
    if len(word) < 3:
        return 0
    word_value = parser(word)
    match word_value:
        case _ if 10000 < word_value <= 100000:
            boost = 50 - (word_value / 10000)
        case _ if 100000 < word_value <= 1000000:
            boost = 40 - (word_value / 100000)
        case _ if 1000000 < word_value <= 100000000:
            boost = 30 - (word_value / 10000000)
        case _ if 100000000 < word_value <= 1000000000:
            boost = 20 - (word_value / 100000000)
        case _ if word_value > 1000000000:
            boost = 10
        case _:
            boost = 0
    if 11 <= len(word) < 20:
        length_factor = 0.8
    elif 20 <= len(word) < 30:
        length_factor = 0.6
    elif len(word) >= 30:
        length_factor = 0.4
    else:
        length_factor = 1
    used_factor = 1
    counter = 1
    for used_word in used_words:
        if used_word.lower() in word.lower() or word.lower() in used_word.lower() and used_factor >= 0.2:
            counter += 1
    print(counter)
    used_factor = used_factor / counter
    logging.info("Input " + word + " stats: word value: " + str(boost) + ", length_factor: " + str(length_factor) + ", used_factor: " + str(used_factor))
    return round((boost * length_factor * used_factor), 2)


def win_score(words):
    return 111 - len(words)
