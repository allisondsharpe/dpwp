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
        page_body = '''
<a href="?email=mickey@disney.com&user=Mickey">Mickey</a><br/>
<a href="?email=donald@disney.com&user=Donald">Donald</a><br/>
<a href="?email=minnie@disney.com&user=Minnie">Minnie</a><br/>
<a href="?email=pluto@disney.com&user=Pluto">Pluto</a>
        '''
        
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
