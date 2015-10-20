'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

import webapp2
from pages import ContentPage
from data import Data, DataObject
from lib import Lib, LibData

class MainHandler(webapp2.RequestHandler):
    def get(self):
        cp = ContentPage() #Creates an instance of ContentPage() class from pages.py
        d = Data() #Creates an instance of Data() class from data.py
        do = DataObject() #Creates an instance of DataObject() class from data.py
        l = Lib() #Creates an instance of Lib() class from lib.py
        ld = LibData() #Creates an instance of LibData() class from lib.py

        if self.request.GET: #Checking to see if we have user input
            nav = self.request.GET['nav']
            if nav == 'home': #(DataObject() and Data())
                do = d.objects[0]
            elif nav == 'about':
                do = d.objects[1]
            elif nav == 'careers':
                do = d.objects[2]
            elif nav == 'faq':
                do = d.objects[3]
            elif nav == 'contact':
                do = d.objects[4]
        else:
            do = d.objects[0] #User will remain on Home

        cp._nav = do.nav
        cp._header = do.header
        cp._the_body = do.the_body
        cp._footer = do.footer
        cp._current_year = do.current_year

        self.response.write(cp.new_print_out()) #New print_out for pages.py

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
