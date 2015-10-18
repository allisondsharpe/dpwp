'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

import webapp2
from pages import ContentPage
from data import Data, DataObject
#from lib import ___

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = ContentPage()
        d = Data()
        do = DataObject()

        if self.request.GET:
            nav = self.request.GET['nav']

            if nav == 'home':
                do = d.list[0]
            elif nav == 'about':
                do = d.list[1]
            elif nav == 'careers':
                do = d.list[2]
            elif nav == 'faq':
                do = d.list[3]
            elif nav == 'contact':
                do = d.list[4]
        else:
            do = d.list[0] #User will be redirected to home page



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
