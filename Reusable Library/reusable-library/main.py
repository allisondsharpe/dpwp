'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''


import webapp2 #Imports webapp for MainHandler() class
from library import Scores, ScoreData #Importing class Scores() and class (ScoreData)
from pages import ResultsPage, FormPage #Importing class ResultsPage() and class FormPage()

class MainHandler(webapp2.RequestHandler): #MainHandler() class
    def get(self):
        s = ScoreData() #Instance created for ScoreData() class

        if self.request.GET:

            s1 = ScoreData() #Instance for s1 created within ScoreData()
            s1.name = self.request.GET['s1_name'] #
            s1.score1 = (self.request.GET['s1_score1'])
            s1.score2 = (self.request.GET['s1_score2'])
            s1.score3 = (self.request.GET['s1_score3'])
            s1.score4 = (self.request.GET['s1_score4'])
            s1.final_score = (self.request.GET['s1_final'])
            s.add_new_competitor(s1)

            s2 = ScoreData()
            s2.name = self.request.GET['s2_name']
            s2.score1 = (self.request.GET['s2_score1'])
            s2.score2 = (self.request.GET['s2_score2'])
            s2.score3 = (self.request.GET['s2_score3'])
            s2.score4 = (self.request.GET['s2_score4'])
            s2.final_score = (self.request.GET['s2_final'])
            s.add_new_competitor(s2)

            s3 = ScoreData()
            s3.name = self.request.GET['s3_name']
            s3.score1 = (self.request.GET['s3_score1'])
            s3.score2 = (self.request.GET['s3_score2'])
            s3.score3 = (self.request.GET['s3_score3'])
            s3.score4 = (self.request.GET['s3_score4'])
            s3.final_score = (self.request.GET['s3_final'])
            s.add_new_competitor(s3)

            s4 = ScoreData()
            s4.name = self.request.GET['s4_name']
            s4.score1 = (self.request.GET['s4_score1'])
            s4.score2 = (self.request.GET['s4_score2'])
            s4.score3 = (self.request.GET['s4_score3'])
            s4.score4 = (self.request.GET['s4_score4'])
            s4.final_score = (self.request.GET['s4_final'])
            s.add_new_competitor(s4)

            s5 = ScoreData()
            s5.name = self.request.GET['s5_name']
            s5.score1 = (self.request.GET['s5_score1'])
            s5.score2 = (self.request.GET['s5_score2'])
            s5.score3 = (self.request.GET['s5_score3'])
            s5.score4 = (self.request.GET['s5_score4'])
            s5.final_score = (self.request.GET['s5_final'])
            s.add_new_competitor(s5)

            rp = ResultsPage() #Instance created for ResultsPage() class - Collects resulting information
            rp.body = (s.calc_score1() + s.calc_score2() + s.calc_score3() + s.calc_score4() + s.calc_final()) #Gathering the results in the body from the ResultsPage() class
            self.response.write(rp.print_out()) #Prints the ResultsPage() class to the browser
        else:
            fp = FormPage() #Instance created for FormPage() class - Collects user input
            self.response.write(fp.print_out()) #Prints the FormPage() class to the browser

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)