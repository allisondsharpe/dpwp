'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

class Page(object):
    def __init__(self):
        self._head = ''' <!-- self.head will serve as the header -->
<!DOCTYPE HTML>
<html>
    <head>
        <title>Sharpe's Inc.</title>
        <link href="css/style.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        '''
        self._body = ''' <!-- self.body will contain the page's content/body -->
        '''
        self._close = ''' <!-- self.close will serve as the footer -->
    </body>
</html> '''

    def print_out(self):
        return self._head + self._body + self._close


class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()

        self._div_container_open = '<div id="container">'
        @property
        def div_container_open(self):
            pass


        self._nav = ''
        @property
        def nav(self):
            pass

        @nav.setter
        def nav(self, new_nav):
            self._nav = new_nav


        self._header = ''
        @property
        def header(self):
            pass

        @header.setter
        def header(self, new_header):
            self._header = new_header



        self._the_body = ''
        @property
        def the_body(self):
            pass

        @the_body.setter
        def the_body(self, new_body):
            self._the_body = new_body



        self._footer = ''
        @property
        def footer(self):
            pass

        @footer.setter
        def footer(self, new_footer):
            self._footer = new_footer



        self._current_year = 0
        @property
        def current_year(self):
            pass

        @current_year.setter
        def current_year(self, new_year):
            self._current_year = new_year



        self._div_container_close = '</div>'

        @property
        def div_container_close(self):
            pass



    #New print_out function - Will overwrite the first one
    def new_print_out(self):
        return self._head + self._body + self._div_container_open + '<a href="?email=allisonsharpe@ymail.com">' + self._nav + '</a>' + '<h1>' + self._header + '</h1>' + '<p>' + self._the_body + '</p>' +  '<p>' + self._footer  + '</p>' + '<p>' + str(self._current_year) + '</p>'  + self._div_container_close + self._close