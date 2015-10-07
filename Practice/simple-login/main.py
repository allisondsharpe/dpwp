'''
Name: Allison Sharpe
Date: 10/2/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

import webapp2 #use webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Catalyst - starts reaction
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title> Simple Form </title>
    </head>
    <body>'''
        page_body = '''<form method="GET">
            <label>Name:</label><input type="text" name="user" />
            <label>Email:</label><input type="text" name="email" />
            <input type="submit" value="Submit" /> '''
        page_close = '''
        </form>
    </body>
</html>'''
        if self.request.GET: #same as == True
            #stores info we got from the form
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_body + page_close) #displays information to browser
        else:
            self.response.write(page_head + page_body + page_close) #printing out information




#makes python work in browser, do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
