#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#

import time

def log(user_name, user_loc, time, what, why, result, hash, logpath):
    """
    Logs information to a file corresponding with the image number i.e. log_1.txt
    :param user_name: name of the user currently using the program
    :param user_loc: location of the user currently using the program
    :param module_name: name of the module where the log comes from
    :param imgnr: number of the image as stated in the database
    :param log_body: Content of the log message
    :return: nothing
    """

    open(logpath, "a+").write(time + "," + user_name + "," + user_loc + "," + what + "," + why + "," + result + "," + hash + '\n')


def error_log(module_name, error_body):
    """
    Logs error information to a Error_log.txt
    :param module_name: name of the module where the log comes from
    :param error_body: Content of the error message
    :return: nothing
    """
    when = time.strftime("%d/%m/%Y" + " " + "%H:%M:%S ")
    data = str(error_body) + "\n"
    open("Error_log.txt", "a+").write(when + module_name + data)
