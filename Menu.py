#! /usr/bin/env python
#
#
#
# Author: Dario
#

import ExceptionHandling
from Logging import Logging
from Scraper import Scrapert
from Buster import Buster


class Menu:
    """
    This class contains the CLI menu and user interaction handling of the program
    """

    def __init__(self):
        """
        This is the constructor of the CLI menu
        :param username: Name of the current user
        :param userloc: location of the user
        :param logpath: Path to the logfile
        """
        self.username = ""
        self.userloc = ""
        self.logpath = ""
        self.entitie = False

    def show_menu(self):
        """
        prints out the menu
        :return: the selected option
        """
        if self.username is "" or self.userloc is "" or self.logpath is "":
            self.username = raw_input("Set username: ")
            self.userloc = raw_input("Set user location: ")
            self.logpath = raw_input("Set full log path:")
            self.entitie = raw_input("Do you want entity extraction instead of text? y/N")
            if self.entitie == "Y" or self.entitie == 'y':
                self.entitie = True
        print ""
        # limit this options if no image is set

        print "1. Scrape website"
        print "2. Run scraper on gobuster output."
        print "3. Enter file with hrefs."
        print "4. exit\n"

        try:
            optionnumber = raw_input("Choose an option number: \n")
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

        # 1. Scrapes page that is given.
        if option == 1:
            website = raw_input("Voer hier de site in die U wil scrapen:\n")
            scraper = Scrapert()
            scraper.scraper(website, self.username, self.userloc, self.logpath, True, self.entitie)

        # Run the option to extract collected links with gobuster.
        if option == 2:
            print "Het bestand moet de volgende naamgeving hebben: Domeinnaam  - tld  - iets .txt voorbeeld nu.nl.gobuster.txt"
            txtfile = raw_input("Voer hier de locatie van het .txt bestand in.\n")
            buster = Buster()
            buster.readfile(txtfile, self.username, self.userloc, self.logpath, True, self.entitie)

        # Run the option to extract collected links to pages on the web server.
        if option == 3:
            print "Het bestand moet de volgende naamgeving hebben: Domeinnaam  - tld  - iets .txt voorbeeld nu.nl.href.txt"
            txtfile = raw_input("Voer hier de locatie van het .txt bestand in.\n")
            buster = Buster()
            buster.readfile(txtfile, self.username, self.userloc, self.logpath, False, self.entitie)

        # Exit the code.
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
