#! /usr/bin/env python
#
#
#
# Author: Dario
#

import ExceptionHandling
import Logging
import Scraper

class Menu:
    """
    This class contains the CLI menu and user interaction handling of the program
    """

    def __init__(self):
        """
        This is the constructor of the CLI menu
        """
        self.username = ""
        self.userloc = ""
        self.logpath = ""

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
        print "2. Exit"

        print ""
        try:
            optionnumber = raw_input("Choose an option number: ")
            # user input handling
            if optionnumber.isdigit() and int(optionnumber) > 0 and int(optionnumber) < 3:
                return int(optionnumber)
            else:
                raise ExceptionHandling.WrongOptionNumber()
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
            text, hash = Scraper.scraper(website, self.username, self.userloc, self.logpath)
            print text
            print hash


def __main__():
    """
    Main program
    :return: nothing
    """
    option = 0
    menu = Menu()
    while option != 2:
        option = menu.show_menu()
        menu.choose_option(option)


__main__()
