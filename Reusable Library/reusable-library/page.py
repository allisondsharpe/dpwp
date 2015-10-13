'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

from lib import Scores


class Page(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/style.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title> Final Scores! </title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.body = ""
        self.__error = ''
        self.__close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all

