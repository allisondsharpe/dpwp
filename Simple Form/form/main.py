'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        if self.request.GET:
            name = self.request.GET['name']
            email = self.request.GET['email']
            address = self.request.GET['address']
            phone = self.request.GET['phone']
            sex = self.request.GET['sex']
            status = self.request.GET['status']
            self.response.write(self.head + name + ' ' + email + ' ' + address + ' ' + phone + ' ' + sex + ' ' + status + ' ' + self.body + self.close)
        else:
            self.response.write(self.head + self.body + self.close)

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/pages', Page)],
    debug=True)
