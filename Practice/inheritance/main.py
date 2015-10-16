
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

class Page(object): #borrowing stuff from the object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body> '''

        self._body = ''
        self._close = '''
    </body>
</html> '''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page): #sub class for Page - Page is super page/parent class to FormPage
    def __init__(self):
        #contructor function for super class/FormPage()
        super(FormPage, self).__init__() #Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        #<input type="text" value="" name="first_name" placeholder="First Name" />
        #<input type="text" value="" name="last_name" placeholder="Last Name" />
        #<input type="submit" value="Submit" />

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
