#! /usr/bin/env python
#
#
#
# Author: Dario
#

import time


class Logging:

    """
    This class contains the Logging function
    """

    def log(self, user_name, user_loc, time, what, why, result, hash, logpath):
        """
        :param user_name: name of the user currently using the program
        :param user_loc: location of the user currently using the program
        :param time: timestamp of this moment.
        :param what: explanation of what the tool is doing.
        :param why: explanation of why it's doing it.
        :param result: The result of te actions.
        :param hash: Hash value of the new file.
        :param logpath: The path to the logfile.
        :return: nothing
        """

        open(logpath, "a+").write(time + "," + user_name + "," + user_loc + "," + what + "," + why + "," + result + "," + hash + '\n')


    def error_log(self, module_name, error_body):
        """
        Logs error information to a Error_log.txt
        :param module_name: name of the module where the log comes from
        :param error_body: Content of the error message
        :return: nothing
        """
        when = time.strftime("%d/%m/%Y" + " " + "%H:%M:%S ")
        data = str(error_body) + "\n"
        open("Error_log.txt", "a+").write(when + module_name + data)
