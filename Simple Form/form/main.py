'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

import webapp2
from pages import Page #imports class Page()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page() #variable for Page()
        self.response.write(p.print_out()) #prints out function "print_out" in class Page()

        if self.request.GET: #retrieves information from Page() to print to browser
            name = self.request.GET['name']
            email = self.request.GET['email']
            address = self.request.GET['address']
            phone = self.request.GET['phone']
            relocation = self.request.GET['relocation']
            dept = self.request.GET['dept']
            self.response.write(name + ' ' + email + ' ' + address + ' ' + phone + ' ' + dept + ' ' + relocation) #prints out results to browser
        else:
            pass

app = webapp2.WSGIApplication([
    (r'/', MainHandler)],
    debug=True)
