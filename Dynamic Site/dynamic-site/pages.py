'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

class Page(object): #Page() class created to contain html template
    def __init__(self):
        self._head = ''' <!-- self.head will open up the template -->
<!DOCTYPE HTML>
<html>
    <head>
        <title>Sharpe's Inc.</title> <!-- Title for Sharpe's Inc. -->
        <link href="css/style.css" rel="stylesheet" type="text/css"> <!-- Link to CSS stylesheet -->
    </head>
    <body>
        '''
        self._body = ''' <!-- self.body will contain the page's content/body -->
         '''
        self._close = ''' <!-- self.close will close out of the template -->
    </body>
</html> '''

    def print_out(self): #The print_out function created for the template
        return self._head + self._body + self._close #Returns self._head, self._body, and self._close


class ContentPage(Page): #ContentPage() class created to contain the getters and setters
    def __init__(self):
        super(ContentPage, self).__init__() #ContentPage() is the sub class to Page()

        #Getter and setter created for '_header_img'
        self._header_img = ''
        @property
        def header_img(self):
            pass

        @header_img.setter
        def header(self, new_header):
            self._header = new_header


        #Getter and setter created for '_header'
        self._header = ''
        @property
        def header(self):
            pass

        @header.setter
        def header(self, new_header):
            self._header = new_header


        #Getter and setter created for '_the_body'
        self._the_body = ''
        @property
        def the_body(self):
            pass

        @the_body.setter
        def the_body(self, new_body):
            self._the_body = new_body


        #Getter and setter created for '_footer'
        self._footer = ''
        @property
        def footer(self):
            pass

        @footer.setter
        def footer(self, new_footer):
            self._footer = new_footer


        #Getter and setter created for '_current_year'
        self._current_year = 0
        @property
        def current_year(self):
            pass

        @current_year.setter
        def current_year(self, new_year):
            self._current_year = new_year


    #New print_out function - Will overwrite the first one
    def new_print_out(self): #Polymorphism function - Will return all values that would otherwise be created within the template
        return self._head + self._body + '<div id="container">' + self._header_img + '<nav>' + '<li><a href="?nav=home" class="btn"> Home </a></li>' + '<li><a href="?nav=about" class="btn"> About </a></li>' + '<li><a href="?nav=careers" class="btn"> Careers </a></li>' + '<li><a href="?nav=faq" class="btn"> FAQ </a></li>' + '<li><a href="?nav=contact" class="btn"> Contact </a></li>' + '</nav>' + '<h1>' + self._header + '</h1>' + '<h2>' + self._the_body + '</h2>' +  '<p id="copyright">' + self._footer  + '</p>' + '<p>' + str(self._current_year) + '</p>'  + '</div>' + self._close