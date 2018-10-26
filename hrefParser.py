#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#


class hrefParser:

    """
    This class contains the CLI menu and user interaction handling of the program
    """

    def parser(self, array, site):
        """
        Parse array to .href.txt file.
        :param array: array with href links.
        :param site: original domain name.
        """
        sites = []
        print site + "              site test"
        # loop through given array
        for x, y in enumerate(array):
            if y.startswith("/"):
                print " test"
                if site.endswith("/"):
                    site = site[:-1]
                url = site + y
                if url in sites:
                    break
                else:
                    sites.append(url)
                    print " append url    " + y
            print y
            if y.__contains__("http") and y.__contains__(site) and not sites.__contains__(y):
                print " append url    " + y
                sites.append(y)

        # write founded links in file.
        site = site.replace("/","-") + ".href.txt"
        f = open(site, "w+")
        for x, y in enumerate(sites):
            if y.__contains__("http"):
                f.write(y + "\n")
            else:
                f.write("http://" + y + "\n")
        f.close()
        print "Bestand " + site + " is aangemaakt."