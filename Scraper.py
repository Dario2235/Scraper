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
import Scp
from PyPDF2 import PdfFileReader
import urllib
from unidecode import unidecode


def scraper(site, user, userloc, logpath):
    text = ""
    what = str(site + " scrapen.")
    when = time.strftime("%d/%m/%Y" + " " + "%H:%M:%S")
    why = "Extract text from the site for research."
    result = str(site + " gescraped. .txt file has been made with the content of the original site.")
    try:
        print site
        if site.__contains__(".pdf"):

            if site.__contains__("www."):
                domain = site.split("www.")
            else:
                domain = site.split("://")
            tld = str(domain[1])
            tld = tld.replace("/", "-")
            filename = "sites/" + tld
            pdffile = download_file(site, filename)
            hex_dig = get_hashes(filename)
            Scp.run(filename)
            Logging.log(user, userloc, when, what, why, result, hex_dig, logpath)
            return(filename, hex_dig)

        else:
            page = requests.get(site)
            if page.status_code == 200:
                soup = BeautifulSoup(page.content, 'html.parser')
                for x, y in enumerate(soup.find_all('p')):
                    text = text + soup.find_all('p')[x].get_text()

                unitext = unidecode(text)
                if site.__contains__("www."):
                    domain = site.split("www.")
                else:
                    domain = site.split("://")
                tld = str(domain[1])
                tld = tld.replace("/", "-")
                f = open(str("sites/" + tld + ".txt"), "w+")
                f.write(unitext)
                f.close()
                filename = "sites/" + tld + ".txt"
                hex_dig = get_hashes(filename)
                Scp.run(filename)
                Logging.log(user, userloc, when, what, why, result, hex_dig, logpath)
                return(unitext, hex_dig)

    except ExceptionHandling.WrongStatusCode as e:
        Logging.error_log("Menu", e.message)
        print "\033[93m" + e.message + "\033[0m"
        pass

def download_file(download_url, filename):
    web_file = urllib.urlopen(download_url)
    local_file = open(filename, 'w')
    local_file.write(web_file.read())
    web_file.close()
    local_file.close()

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        print info
        print number_of_pages

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

