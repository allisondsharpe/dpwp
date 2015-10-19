'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

class Data(object):
    def __init__(self):
        home = DataObject() #Home object instantiated in Data() class for DataObject() class

        home.header_img = ''
        home.header = 'Welcome'
        home.the_body = 'Click a Link Above to Get Started'
        home.footer = 'Copyright'
        home.current_year = 2015

        about = DataObject() #About object instantiated in Data() class for DataObject() class

        about.header_img = ''
        about.header = 'Welcome'
        about.the_body = 'Click a Link Above to Get Started'
        about.footer = 'Copyright'
        about.current_year = 2015

        careers = DataObject() #Careers object instantiated in Data() class for DataObject() class

        careers.header_img = ''
        careers.header = 'Welcome'
        careers.the_body = 'Click a Link Above to Get Started'
        careers.footer = 'Copyright'
        careers.current_year = 2015

        faq = DataObject() #FAQ object instantiated in Data() class for DataObject() class

        faq.header_img = ''
        faq.header = 'Welcome'
        faq.the_body = 'Click a Link Above to Get Started'
        faq.footer = 'Copyright'
        faq.current_year = 2015

        contact = DataObject() #Contact object instantiated in Data() class for DataObject() class

        contact.header_img = 'images/cat.jpg'
        contact.header = 'Welcome'
        contact.the_body = 'Click a Link Above to Get Started'
        contact.footer = 'Copyright'
       	contact.current_year = 2015


        self.objects = [home, about, careers, faq, contact]

class DataObject(object): #DataObject() class
    def __init__(self): #Declaring attributes used in Data() class for objects of DataObject()
        self.header_img = ''
        self.header = ''
        self.the_body = ''
        self.footer = ''
        self.current_year = 0
