#! /usr/bin/env python
#
#
#
# Author: Dario
#


class ExceptionTemplate(Exception):
    def __init__(self):
        Exception.__init__(self, "Error message")

class WrongStatusCode(AttributeError):
    def __init__(self):
        Exception.__init__(self, "Site is not readable, No status code 200")
