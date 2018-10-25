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
        # loop through given array
        for x, y in enumerate(array):
            if y.startswith("/"):
                if site.endswith("/"):
                    site = site[:-1]
                url = site + y
                if url in sites:
                    break
                else:
                    sites.append(url)
                    print " append url    " + y

        # write founded links in file.
        site = site.replace("/","-") + ".href.txt"
        f = open(site, "w+")
        for x, y in enumerate(sites):
            f.write("http://" + y + "\n")
        f.close()
        print "Bestand " + site + " is aangemaakt."