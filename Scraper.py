#! /usr/bin/env python
#
#
#
# Author: Dario
#

import time
import requests
from bs4 import BeautifulSoup
import hashlib
import ExceptionHandling
from Logging import Logging
from Scp import Scp
from Rosette import Rosette
from hrefParser import hrefParser
import urllib
from unidecode import unidecode


class Scrapert:

    """
    This class contains the CLI menu and user interaction handling of the program
    """

    def scraper(self, site, user, userloc, logpath, hrefCheck, entitie):
        """
        This function scrapes the pages.
        :param site: Url from site
        :param user: User who uses the scraper
        :param userloc: Location of the current user
        :param logpath: Path of the log file.
        :param hrefCheck: Check if its the first time in the scraper.
        :param entitie: Check if the entities need to be extracted.
        :return: The filename and the SHA 256 value.
        """
        text = ""
        href = []
        what = str(site + " scrapen.")
        when = time.strftime("%d/%m/%Y" + " " + "%H:%M:%S")
        why = "Extract text from the site for research."
        result = str(site + " gescraped. .txt file has been made with the content of the original site.")
        if str(site).endswith("\n"):
            site = site[:-1]
        try:
            print site
            scp = Scp()
            logging = Logging()
            HrefParser = hrefParser()
            if site.__contains__(".pdf"):

                # Download pdf and push it to the server
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

                # Download the page
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
                filename = self.get_filname(domain, unitext)
                hex_dig = self.get_hashes(filename)
                if entitie:
                    self.get_entities(filename, domain)
                scp.run(filename)
                logging.log(user, userloc, when, what, why, result, hex_dig, logpath)

                # Check if its the first scan.
                if hrefCheck == True and entitie == False:
                    HrefParser.parser(href, str(domain[1]))
                print "SHA 256 : " + hex_dig + "\n"

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

    def get_filname(self, domain, unitext):
        """
        Write text and get filename
        :param domain: toplevel domain
        :param unitext: Text to write in the file.
        :return: The file name that is created.
        """
        tld = str(domain[1])
        tld = tld.replace("/", "-")
        f = open(str("sites/" + tld + ".txt"), "w+")
        f.write(unitext)
        f.close()
        return ("sites/" + tld + ".txt")


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

    def get_entities(self, filename, domain):
        """
        Get enitities in the file.
        :param filename: name of the file
        :param domain: The top level domain.
        :return: nothing
        """
        rosette = Rosette()
        entities = rosette.main(filename)
        self.get_filname(domain, entities)