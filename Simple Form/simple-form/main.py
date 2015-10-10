'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

import webapp2 #Imports webapp2 for MainHandler() to work
from page import Page #Imports class Page()

class MainHandler(webapp2.RequestHandler): #Official MainHandler class
    def get(self):

        if self.request.GET: #GET delivers the variables to the page
            page = Page(self)  #Retrieves Page()
            #Retrieves information from Page to be printed to browser
            data = self.request.GET["name"] + ' ' + self.request.GET["email"] + ' ' + self.request.GET["address"] + ' ' + self.request.GET["phone"] + ' ' + self.request.GET["relocate"] + ' ' + self.request.GET["dept"]
            self.response.write(page.print_info(data)) #Prints information to the browser
        else:
            page = Page(self) #Retrieves Page()
            self.response.write(page.print_info()) #Prints information to the browser

app = webapp2.WSGIApplication([ #Enables webapp2 for MainHandler()
    ('/', MainHandler)
], debug=True)