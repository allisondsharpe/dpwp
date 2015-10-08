'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.title = "Welcome!"
        self.css = "css/style.css"
        self.head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="Stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self.body = ''' <form method="GET">
            <label>Name:</label><input type="text" name="name" /><br/><br/>
            <label>Email:</label><input type="text" name="email" /><br/><br/>
            <label>Address:</label><input type="text" name="address" /><br/><br/>
            <label>Phone Number:</label><input type="text" name="phone" /><br/><br/>
            <label>Gender:
                <input type="radio" name="sex" value="male" checked>Male
                <input type="radio" name="sex" value="female">Female <br/><br/>
            </label>
            <label>Employment Status:
                <select name="status">
                    <option value="employed">Employed</option>
                    <option value="unemployed">Unemployed</option>
                    <option value="student">Student</option>
                    <option value="laid-off">Laid Off</option>
                </select><br/><br/>
            </label>
            <input type="submit" value="Submit" /> '''
        self.close = '''
        </form>
    </body>
</html>
        '''

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
    ('/', MainHandler)
], debug=True)
