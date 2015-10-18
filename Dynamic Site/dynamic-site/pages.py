'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

class Page(object): #Template HTML - Super Class to ContentPage
    def __init__(self):
        self.__title = "Sharpe's Inc." #Private attribute for self.__title
        self.css = "css/style.css" #Attribute for self.css
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Sharpe's Inc.</title>
        <link href="css/style.css" rel="stylesheet" type="text/css">
    </head>
    <body> '''

        self._body = 'Hello'
        self._close = '''
    </body>
</html> '''

    def print_out(self):
        return self._head + self._body + self._close

class ContentPage(Page): #sub class for Page - Page is super page/parent class to ContentPage
    def __init__(self):
        #contructor function for super class/FormPage()
        super(ContentPage, self).__init__() #Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        #<input type="text" value="" name="first_name" placeholder="First Name" />
        #['first_name'<-- placeholder, text,<-- text 'First Name'<-- value]
        #<input type="text" value="" name="last_name" placeholder="Last Name" />
        #<input type="submit" value="Submit" />

    @property
    def inputs(self):
       pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        #sort through the mega array and create HTML inputs based on the info there
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a third item.. add it in..
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            #otherwise.. end the tag
            except:
                self._form_inputs += '" />'

            print self._form_inputs

    def print_out_form(self):
       return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close
