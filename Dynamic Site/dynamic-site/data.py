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
        home.header = "Welcome to the Home Page of Sharpe's Inc."
        home.the_body = 'To get started, browse our navigational items above.'
        home.footer = "Copyright Sharpe's Inc."
        home.current_year = 2015

        about = DataObject() #About object instantiated in Data() class for DataObject() class
        about.header_img = ''
        about.header = "About Sharpe's Inc."
        about.the_body = "Sharpe's Inc. has been helping people for more than twenty years..."
        about.footer = "Copyright Sharpe's Inc."
        about.current_year = 2015

        careers = DataObject() #Careers object instantiated in Data() class for DataObject() class
        careers.header_img = ''
        careers.header = "Would You Be Interested in Working With Us?"
        careers.the_body = 'Submit a form within the contact section and let us know!'
        careers.footer = "Copyright Sharpe's Inc."
        careers.current_year = 2015

        faq = DataObject() #FAQ object instantiated in Data() class for DataObject() class
        faq.header_img = ''
        faq.header = "Welcome to Our FAQ's Page"
        faq.the_body = 'Q: What does your company do? </br> A: It helps to provide others with..'
        faq.footer = "Copyright Sharpe's Inc."
        faq.current_year = 2015

        contact = DataObject() #Contact object instantiated in Data() class for DataObject() class
        contact.header_img = ''
        contact.header = "Want to Contact Us?"
        contact.the_body = 'Submit your form and a representative will be in touch with you soon.'
        contact.footer = "Copyright Sharpe's Inc."
       	contact.current_year = 2015


        self.objects = [home, about, careers, faq, contact]

class DataObject(object): #DataObject() class
    def __init__(self): #Declaring attributes used in Data() class for objects of DataObject()
        self.header_img = ''
        self.header = ''
        self.the_body = ''
        self.footer = ''
        self.current_year = 0
