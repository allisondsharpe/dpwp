'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

import webapp2
from lib import Scores
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #Jason's scores
        j = Scores()
        j.score1 = 50
        j.score2 = 30
        j.score3 = 65
        j.score4 = 80
        j.final_score = 95
        self.response.write("Jason's final score is " + str(j.final_score))

        #Vaas' scores
        v = Scores()
        v.score1 = 20
        v.score2 = 45
        v.score3 = 60
        v.score4 = 75
        v.final_score = 80
        self.response.write("<br /> Vaas' final score is " + str(v.final_score))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
