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
from Logging import Logging
from Scp import Scp
from hrefParser import hrefParser
from PyPDF2 import PdfFileReader
import urllib
from unidecode import unidecode


class Scrapert:

    """
    This class contains the CLI menu and user interaction handling of the program
    """

    def scraper(self, site, user, userloc, logpath, hrefCheck):
        """
        This function scrapes the pages.
        :param site: Url from site
        :param user: User who uses the scraper
        :param userloc: Location of the current user
        :param logpath: Path of the log file.
        :param hrefCheck: Check if its the first time in the scraper.
        :return: nothing
        """
        text = ""
        href = []
        what = str(site + " scrapen.")
        when = time.strftime("%d/%m/%Y" + " " + "%H:%M:%S")
        why = "Extract text from the site for research."
        result = str(site + " gescraped. .txt file has been made with the content of the original site.")
        if str(site).endswith("\n"):
            site = site[:-2]
        try:
            print site
            scp = Scp()
            logging = Logging()
            HrefParser = hrefParser()
            if site.__contains__(".pdf"):

                #Download pdf and push it to the server
                if site.__contains__("www."):
                    domain = site.split("www.")
                else:
                    domain = site.split("://")
                tld = str(domain[1])
                tld = tld.replace("/", "-")
                filename = "sites/" + tld
                # scraper = Scraper.scraper()
                self.download_file(site, filename)
                hex_dig = self.get_hashes(filename)

                scp.run(filename)
                # Write logging to .csv file.

                logging.log(user, userloc, when, what, why, result, hex_dig, logpath)
                return(filename, hex_dig)

            else:
                #Download the page
                page = requests.get(site)

                soup = BeautifulSoup(page.content, 'html.parser')

                # Extract all P tags
                for x, y in enumerate(soup.find_all('p')):
                    text = text + soup.find_all('p')[x].get_text()
                # Extract all href's
                for a in soup.find_all('a', href=True):
                    href.append(a['href'])

                # Parse text to unicode.
                unitext = unidecode(text)
                if site.__contains__("www."):
                    domain = site.split("www.")
                else:
                    domain = site.split("://")

                # Write text to .txt file
                tld = str(domain[1])
                tld = tld.replace("/", "-")
                f = open(str("sites/" + tld + ".txt"), "w+")
                f.write(unitext)
                f.close()
                filename = "sites/" + tld + ".txt"
                hex_dig = self.get_hashes(filename)
                scp.run(filename)
                logging.log(user, userloc, when, what, why, result, hex_dig, logpath)

                # Check if its the first scan.
                if hrefCheck == '0':
                    HrefParser.parser(href, str(domain[1]))
                print hex_dig
                return

        except ExceptionHandling.WrongStatusCode as e:
            Logging.error_log("Menu", e.message)
            print "\033[93m" + e.message + "\033[0m"
            pass

    # Download function for pdf files.
    def download_file(self, download_url, filename):
        """
        Download pdf file
        :param download_url: url of the pdf file
        :param filename: Name of the file.
        :return: Nothing
        """
        web_file = urllib.urlopen(download_url)
        local_file = open(filename, 'w')
        local_file.write(web_file.read())
        web_file.close()
        local_file.close()

    # Get pfd information
    def get_info(self, path):
        """
        Get pdf information
        :param path: The path to the pdf file.
        :return: Nothing
        """
        with open(path, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            print info
            print number_of_pages

    def get_hashes(self, file):
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
