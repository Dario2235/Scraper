#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#

def parser(array, site):
    sites = []
    for x, y in enumerate(array):
        aTag = y.split(" ")
        for xx, y in enumerate(aTag):
            if aTag[xx].__contains__("href"):
                link = str(aTag[xx])
                link = link.split("\"")
                if link[1].startswith("/"):
                    if site.endswith("/"):
                        site = site[:-1]
                    url = site + link[1]
                    sites.append(url)

    site = site + ".txt"
    f = open(site, "w+")
    for x, y in enumerate(sites):
        f.write("http://" + y + "\n")
    f.close()