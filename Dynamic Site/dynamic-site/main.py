'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''


import webapp2
from pages import ContentPage
from data import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = ContentPage()
        p.inputs = [['first_name', 'text','First Name'], ['last_name', 'text','Last Name'], ['Submit', 'submit']]
        self.response.write(p.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
