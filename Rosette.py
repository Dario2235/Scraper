#! /usr/bin/env python
#
#
#
# Author: Dario
#

import argparse
import json
import os

from rosette.api import API, DocumentParameters, RosetteException


class Rosette:
    """
    This class contains the funtions to use the Rosette API.
    """

    PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Calls the ' +
                                                 os.path.splitext(os.path.basename(__file__))[0] + ' endpoint')
    PARSER.add_argument('-k', '--key', help='Rosette API Key', required=False)
    PARSER.add_argument('-u', '--url', help="Alternative API URL",
                        default='https://api.rosette.com/rest/v1/')

    def __init__(self):
        """
       This is the constructor of the Rosette Script
       :param key: The Rosette API key
       """
        # Enter here your Rosette API key
        self.key = ""


    def run(self, txtfile, alt_url='https://api.rosette.com/rest/v1/'):
        """
        Set up connection to the API and receives the founded entities.
        :param txtfile: Name of the file with scraped text.
        :return: entities in JSON format.
        """
        # Create an API instance
        print self.key
        api = API(user_key=self.key, service_url=alt_url)

        lines = ""
        f = open(txtfile)
        for x, y in enumerate(f):
            if y.__contains__("."):
                lines = lines + str(y)
        f.close()
        params = DocumentParameters()
        params["content"] = lines
        try:
            return api.entities(params)
        except RosetteException as exception:
            print(exception)

    def main(self, txtfile):
        """
        Main function of Rosette functionality.
        :param txtfile: Name of the file with scraped text.
        :return: JSON output of Rosette.
        """

        rosette = Rosette()
        args = rosette.PARSER.parse_args()
        result = rosette.run(txtfile, args.url)
        return (json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True).encode("utf8"))

