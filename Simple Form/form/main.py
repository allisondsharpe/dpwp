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
        self.response.write(p.print_out())

        if self.request.GET:
            name = self.request.GET['name']
            email = self.request.GET['email']
            address = self.request.GET['address']
            phone = self.request.GET['phone']
            sex = self.request.GET['sex']
            status = self.request.GET['status']
            self.response.write(p.head + name + ' ' + email + ' ' + address + ' ' + phone + ' ' + sex + ' ' + status + p.body + p.close)
        else:
            pass

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/pages', Page)],
    debug=True)
