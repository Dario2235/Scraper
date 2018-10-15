#! /usr/bin/env python
#
#
#
# Author: Dario
#

import ExceptionHandling
import Logging
import Scraper
import Buster

class Menu:
    """
    This class contains the CLI menu and user interaction handling of the program
    """

    def __init__(self):
        """
        This is the constructor of the CLI menu
        """
        self.username = "dario"
        self.userloc = "huis"
        self.logpath = "log1.csv"


    def show_menu(self):
        """
        prints out the menu
        :return: the selected option
        """
        if self.username is "" or self.userloc is "" or self.logpath is "":
            self.username = raw_input("Set username: ")
            self.userloc = raw_input("Set user location: ")
            self.logpath = raw_input("Set full log path:")
        print ""
        # limit this options if no image is set

        print "1. Scrape website"
        print "2. Run scraper on gobuster output."
        print "3. Voer bestand met href's in."
        print "4. exit"

        print ""
        try:
            optionnumber = raw_input("Choose an option number: ")
            # user input handling
            if optionnumber.isdigit() and int(optionnumber) > 0 and int(optionnumber) < 5:
                return int(optionnumber)
        except ExceptionHandling.WrongOptionNumber as e:
            Logging.error_log("Menu", e.message)
            print "\033[93m" + e.message + "\033[0m"
            pass

    def choose_option(self, option):
        """
        Handling of the selected option
        :param option: the selected option
        :return: nothing
        """

        # 1. Select URL
        if option == 1:
            website = raw_input("Voer hier de site in die U wil scrapen:")
            Scraper.scraper(website, self.username, self.userloc, self.logpath, '0')

        # Voer text bestand in met de output van gobuster
        if option == 2:
            txtfile = raw_input("Voer hier de locatie van het .txt bestand in.")
            Buster.readfile(txtfile, self.username, self.userloc, self.logpath, '0')

        # Voer text bestand in met aangemaakte href bestand.
        if option == 3:
            print "Het bestand moet de volgende naamgeving hebben: Domeinnaam  - tld  - iets .txt voorbeeld nu.nl.test.txt"
            txtfile = raw_input("Voer hier de locatie van het .txt bestand in.")
            Buster.readfile(txtfile, self.username, self.userloc, self.logpath, '1')

        # Verlaat het programma
        if option == 4:
            exit()

def __main__():
    """
    Main program
    :return: nothing
    """
    option = 0
    menu = Menu()
    while option != 4:
        option = menu.show_menu()
        menu.choose_option(option)


__main__()
