'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

import webapp2
from lib import Students, StudentData
from page import ResultsPage, FormPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        sd = StudentData() #Instance of ScoreData()
        rp = ResultsPage() #Instance of ResultsPage

        if self.request.GET:
            s1 = Students()
            s1.first_name = self.request.GET['s1_first']
            s1.last_name = (self.request.GET['s1_last'])
            s1.grade_level = int(self.request.GET['s1_level'])
            s1.gpa = int(self.request.GET['s1_gpa'])
            sd.add_student(s1)

            s2 = Students()
            s2.first_name = self.request.GET['s2_first']
            s2.last_name = (self.request.GET['s2_last'])
            s2.grade_level = int(self.request.GET['s2_level'])
            s2.gpa = int(self.request.GET['s2_gpa'])
            sd.add_student(s2)

            s3 = Students()
            s3.first_name = self.request.GET['s3_first']
            s3.last_name = (self.request.GET['s3_last'])
            s3.grade_level = int(self.request.GET['s3_level'])
            s3.gpa = int(self.request.GET['s3_gpa'])
            sd.add_student(s1)

            rp.body = (sd.calc_first() + sd.calc_last() +  sd.calc_level() + sd.calc_gpa())
            self.response.write(rp.print_out())

        else:
            rp = FormPage()
            self.response.write(rp.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
