#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#
import Scraper

def readfile(file, username, userloc, logpath, option):
    f = open(file, 'r')
    lines = f.readlines()
    print lines
    for x, y in enumerate(lines):
        print lines[x]
        if lines[x].__contains__("Status: 200"):
            line = lines[x].split(" ")
            site = "http://www." + file.split(".")[0] + "." + file.split(".")[1] + line[0]
            Scraper.scraper(site, username, userloc, logpath, option)
        if option == '1':
            Scraper.scraper(lines[x], username, userloc, logpath, option)