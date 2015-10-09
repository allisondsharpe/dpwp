'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

class Page(object): #class Page() created for form
    def __init__(self): #function for class Page()
        self.title = "Sharpe's Inc." #title
        self.css = "css/style.css" #css stylesheet
        self.head = '''<!DOCTYPE HTML> <!-- html begins here -->
<html>
    <head>
        <title>Sharpe's Inc. - Apply Today</title> <!-- Sharpe's Inc. is a made up company -->
        <link href="{self.css}" rel="Stylesheet" type="text/css" /> <!-- link to my stylesheet -->
    </head>
    <body>
        '''
        self.body = '''<form method="GET">
            <h1> Sharpe's Inc. Application Form </h1> <!-- header -->
            <p> Fill out the form below to get started. </p>
            <label>Name:</label><input type="text" name="name" class="fields"/><br/><br/> <!-- collects name of user -->
            <label>Email:</label><input type="text" name="email" class="fields"/><br/><br/> <!-- collects email of user -->
            <label>Address:</label><input type="text" name="address" class="fields"/><br/><br/> <!-- collects address of user -->
            <label>Phone:</label><input type="text" name="phone" class="fields" /><br/><br/> <!-- collects phone number of user -->
            <label>Job Dept: <!-- select options for job department -->
                <select name="dept">
                    <option value="head">Headquarters</option>
                    <option value="office">Distribution Centers</option>
                </select><br/><br/>
            </label>
            <label>Would you be willing to relocate if required? <!-- radio option for relocation -->
                <input type="radio" name="relocate" value="delivered" checked> Yes
                <input type="radio" name="relocate" value="pickup" checked> No <br/><br/>
            </label>
            <a href="../new-page.py"><input type="submit" id="submit" value="Submit"></a> <!-- submit button for form -->'''
        self.close = '''
        </form>
    </body>
</html>
        '''

    def print_out(self):
        all = self.head + self.body + self.close #retrieves self.head, self.body, and self.close from html
        all = all.format(**locals())
        return all #returns variable 'all'

