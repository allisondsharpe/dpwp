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


        self._header_img = ''
        @property
        def header_img(self):
            pass

        @header_img.setter
        def header(self, new_header):
            self._header = new_header


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
        return self._head + self._body + self._div_container_open + self._header_img + '<nav>' + '<li><a href="?nav=home"> Home </a></li>' + '<li><a href="?nav=about"> About </a></li>' + '<li><a href="?nav=careers"> Careers </a></li>' + '<li><a href="?nav=faq"> FAQ </a></li>' + '<li><a href="?nav=contact"> Contact </a></li>' + '</nav>' + '<h1>' + self._header + '</h1>' + '<h2>' + self._the_body + '</h2>' +  '<p>' + self._footer  + '</p>' + '<p>' + str(self._current_year) + '</p>'  + self._div_container_close + self._close