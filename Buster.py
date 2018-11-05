#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#
from Scraper import Scrapert


class Buster:

    """
    This class contains the function to scrape sites form a .txt file.
    """

    def readfile(self, filename, username, userloc, logpath, option, entitie):
        """
        Read the file with links
        :param filename: Name of the file to be read.
        :param username: Name of the current user.
        :param userloc: Location of the current user.
        :param logpath: Path to the log file.
        :param option: Option number
        :return: Nothing
        """
        print""
        f = open(filename, 'r')
        lines = f.readlines()
        for x, y in enumerate(lines):
            scraper = Scrapert()
            if option == False:
                scraper.scraper(lines[x], username, userloc, logpath, option, entitie)
            if lines[x].__contains__("Status: 200"):
                line = lines[x].split(" ")
                site = "http://www." + filename.split(".")[0] + "." + filename.split(".")[1] + line[0]
                scraper.scraper(site, username, userloc, logpath, False, entitie)