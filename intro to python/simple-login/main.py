'''
Name: Allison Sharpe
Date: 10/2/15
Class:
Assignment: 
'''

import webapp2 #use webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Catalyst - starts reaction
        self.response.write('Hello world!')
        #code goes here
        
    def additional_functions(self):
      	pass
     	#code goes here   


#makes python work in browser, do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
