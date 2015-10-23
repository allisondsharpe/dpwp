'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

import webapp2
from pages import ContentPage
from data import Data, DataObject

class MainHandler(webapp2.RequestHandler): #MainHandler() class = Base class
    def get(self):
        cp = ContentPage() #Creates an instance of ContentPage() class from pages.py
        d = Data() #Creates an instance of Data() class from data.py
        do = DataObject() #Creates an instance of DataObject() class from data.py

        if self.request.GET: #Checking to see if we have user input
            nav = self.request.GET['nav'] #Sending a request to get 'nav'
            if nav == 'home':
                do = d.objects[0] #Redirects the user to the 'home' page
            elif nav == 'about':
                do = d.objects[1] #Redirects the user to the 'about' page
            elif nav == 'careers':
                do = d.objects[2] #Redirects the user to the 'careers' page
            elif nav == 'faq':
                do = d.objects[3] #Redirects the user to the 'faq' page
            elif nav == 'contact':
                do = d.objects[4] #Redirects the user to the 'contact' page
        else:
            do = d.objects[0] #With no input, user will redirect to home page

        cp._header_img = do.header_img #ContentPage() _header_img object created from DataObject() class
        cp._header = do.header #ContentPage() _header object created from DataObject() class
        cp._the_body = do.the_body #ContentPage() _the_body object created from DataObject() class
        cp._footer = do.footer #ContentPage() _footer object created from DataObject() class
        cp._current_year = do.current_year #ContentPage() _current_year object created from DataObject() class
        cp._input = do.input #ContentPage() _input object created from DataObject() class

        self.response.write(cp.new_print_out()) #New print_out for pages.py

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
