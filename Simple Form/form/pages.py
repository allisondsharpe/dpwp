'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/style.css"
        self.head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Sharpe's Supplies - Apply Today</title> <!-- Sharpe's Supplies is a made up company that sells supplies -->
        <link href="{self.css}" rel="Stylesheet" type="text/css" /> <!-- link to my stylesheet -->
    </head>
    <body>
        '''
        self.body = '''

        <h1> Welcome to Sharpe's Supplies </h1> <!-- header -->

        <form method="GET">
            <label>Name:</label><input type="text" name="name" class="fields"/><br/><br/> <!-- collects name of user -->
            <label>Email:</label><input type="text" name="email" class="fields"/><br/><br/> <!-- collects email of user -->
            <label>Address:</label><input type="text" name="address" class="fields"/><br/><br/> <!-- collects address of user -->
            <label>Phone:</label><input type="text" name="phone" class="fields" /><br/><br/> <!-- collects phone number of user -->
            <label>Supply Dept: <!-- select options for supply department -->
                <select name="dept">
                    <option value="home">Home</option>
                    <option value="office">Office</option>
                    <option value="kitchen">Kitchen</option>
                    <option value="outdoor">Outdoor</option>
                </select><br/><br/>
            </label>
            <label>Shipping: <!-- radio option for shipping -->
                <input type="radio" name="shipping" value="delivered" checked>Delivered
                <input type="radio" name="shipping" value="pickup" checked>Pick-up<br/><br/>
            </label>
            <a target="_blank"><input type="submit" id="submit" value="Submit"></a> <!-- submit button for form -->'''
        self.close = '''
        </form>
    </body>
</html>
        '''

    def print_out(self):
        all = self.head + self.body + self.close #retrieves self.head, self.body, and self.close from html
        all = all.format(**locals())
        return all

