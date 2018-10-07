#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#


class ExceptionTemplate(Exception):
    def __init__(self):
        Exception.__init__(self, "Error message")

class WrongStatusCode(AttributeError):
    def __init__(self):
        Exception.__init__(self, "Site is not readable, No status code 200")


class AttrErrorIP(AttributeError):
    def __init__(self):
        Exception.__init__(self, "Attribute error catched, probably IPv6 packet.")


class GenError(Exception):
    def __init__(self):
        Exception.__init__(self, "Unknown error catched, probably a timeout error.")


class NoFileSelected(AttributeError):
    def __init__(self):
        Exception.__init__(self, "No image selected")


class WrongImageExtension(Exception):
    def __init__(self):
        Exception.__init__(self, "No 001 format image selected")


class FileDoesNotExist(Exception):
    def __init__(self):
        Exception.__init__(self, "File does not exist")


class WrongOptionNumber(Exception):
    def __init__(self):
        Exception.__init__(self, "Choose a correct option number")


class FileHasNoMeta(Exception):
    def __init__(self, filename):
        Exception.__init__(self, "File " + filename + " has no meta information and is not added to the list")

class FileOpenMail(IOError):
    def __init__(self):
        IOError.__init__(self, "Please close mail.csv before continuing.")