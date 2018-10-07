#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#

import time
import requests
from bs4 import BeautifulSoup
import hashlib
import ExceptionHandling
import Logging
from unidecode import unidecode


def scraper(site, user, userloc, logpath):
    text = ""
    what = str(site + " scrapen.")
    when = time.strftime("%d/%m/%Y" + " " + "%H:%M:%S")
    why = "Extract text from the site for research."
    result = str(site + " gescraped. .txt file has been made with the content of the original site.")
    try:
        page = requests.get(site)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            for x, y in enumerate(soup.find_all('p')):
                text = text + soup.find_all('p')[x].get_text()
            print text
            unitext = unidecode(text)
            domain = site.split("://")
            print domain[1]
            print
            f = open(str(domain[1] + ".txt"), "w+")
            f.write(unitext)
            f.close()
            hex_dig = get_hashes(domain[1] + ".txt")
            Logging.log(user, userloc, when, what, why, result, hex_dig, logpath)
            return(unitext, hex_dig)

    except ExceptionHandling.WrongStatusCode as e:
        Logging.error_log("Menu", e.message)
        print "\033[93m" + e.message + "\033[0m"
        pass


def get_hashes(file):
    """
    Get hashes of files
    :param file: list of files
    :return: hash value
    """
    sha256 = hashlib.sha256()
    block_size = 65536
    with open(file, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    hash = sha256.hexdigest()
    return hash