'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

class Data(object): #Data() class created to contain objects and attributes created within those objects for DataObject() class
    def __init__(self):

        home = DataObject() #Home object instantiated in Data() class for DataObject() class - Attributes for header_img, header, the_body, footer, and current_year have been created for this object
        home.header_img = ''
        home.header = "Welcome to the Home Page of Sharpe's Inc."
        home.the_body = "We appreciate your interest at Sharpe's Inc. To get started, try browsing our navigational items above."
        home.footer = "Copyright Sharpe's Inc."
        home.current_year = 2015

        about = DataObject() #About object instantiated in Data() class for DataObject() class - Attributes for header_img, header, the_body, footer, and current_year have been created for this object
        about.header_img = ''
        about.header = "About Sharpe's Inc."
        about.the_body = "Sharpe's Inc has been around for more than 20 years for assisting clients with their financial instabilities as well as granting individuals with the ability to work in a safe and drug-free environment. "
        about.footer = "Copyright Sharpe's Inc."
        about.current_year = 2015

        careers = DataObject() #Careers object instantiated in Data() class for DataObject() class - Attributes for header_img, header, the_body, footer, and current_year have been created for this object
        careers.header_img = ''
        careers.header = "Join Our Team"
        careers.the_body = "We are currently hiring now. If you would like to join our team please submit your email in the contact section above and we'll get in touch with you as soon as possible."
        careers.footer = "Copyright Sharpe's Inc."
        careers.current_year = 2015

        faq = DataObject() #FAQ object instantiated in Data() class for DataObject() class - Attributes for header_img, header, the_body, footer, and current_year have been created for this object
        faq.header_img = ''
        faq.header = "Welcome to Our FAQ's Page"
        faq.the_body = "Q: <strong>What are the responsibilities of Sharpe's Inc?</strong> </br> A: We aide our clients with their financial situation and we ensure that everyone gets treated equally and receives the assistance that they deserve.  </br></br> Q: <strong>What should I expect when working for this company?</strong> </br> A: A great atmosphere surrounded by co-workers who enjoy their job and are willing to serve their clients by meeting their needs."
        faq.footer = "Copyright Sharpe's Inc."
        faq.current_year = 2015

        contact = DataObject() #Contact object instantiated in Data() class for DataObject() class - Attributes for header_img, header, the_body, footer, current_year, and input have been created for this object
        contact.header_img = ''
        contact.header = "Want to Contact Us?"
        contact.the_body = 'Submit your email below and a representative will be in touch with you soon.'
        contact.footer = "Copyright Sharpe's Inc."
       	contact.current_year = 2015
        contact.input = '<form><input type="text" id="input"/><input type="button" value="Submit" id="form_btn"/></form>'

        self.objects = [home, about, careers, faq, contact] #Array for 'objects' created to contain each object created within the Data() class

class DataObject(object): #DataObject() class created to contain declarations of attributes created within the Data() class
    def __init__(self):
        #Declaring attributes used in Data() class for objects of DataObject()
        self.header_img = ''
        self.header = ''
        self.the_body = ''
        self.footer = ''
        self.current_year = 0
        self.input = ''
