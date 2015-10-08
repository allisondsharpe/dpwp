'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

import webapp2
from form import Form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Form()

        if self.request.GET:
            name = self.request.GET['name']
            email = self.request.GET['email']
            address = self.request.GET['address']
            phone = self.request.GET['phone']
            sex = self.request.GET['sex']
            status = self.request.GET['status']
            self.response.write(page_head + name + ' ' + email + ' ' + address + ' ' + phone + ' ' + sex + ' ' + status + ' ' + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
