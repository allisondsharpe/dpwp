#adding html and styles

import webapp2
from pages import Page #from package import Class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = "Miss Piggy likes Kermit De Frog!" #modify body element
        print p.print_out()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
