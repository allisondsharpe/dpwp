'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

import webapp2 
from page import Page #imports class Page()

class MainHandler(webapp2.RequestHandler): #MainHandler class 
    def get(self):    

        if self.request.GET:
        	#retrieves information from Page to be printed to browser 
            data = self.request.GET["name"] + ' ' + self.request.GET["email"] + ' ' + self.request.GET["address"] + ' ' + self.request.GET["phone"] + ' ' + self.request.GET["relocate"] + ' ' + self.request.GET["dept"] 
            page = Page(self)  #retrieves page information
            self.response.write(page.print_info(data)) #prints information to browser
        else:
            page = Page(self) #retrieves page information
            self.response.write(page.print_info()) #prints information to browser
            
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)