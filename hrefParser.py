#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#

def parser(array, site):
    sites = []
    # loop door het mee gegeven  array
    for x, y in enumerate(array):

        #print y + " y"
        if y.startswith("/"):
            if site.endswith("/"):
                site = site[:-1]
            url = site + y
            if url in sites:
                break
            else:
                sites.append(url)
                print " append url    " + y

    # Schrijf de gevonden waarden weg in een .txt bestand
    site = site.replace("/","-") + ".href.txt"
    f = open(site, "w+")
    for x, y in enumerate(sites):
        f.write("http://" + y + "\n")
    f.close()
    print "Bestand " + site + " is aangemaakt."