'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

class Form():
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/style.css"
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title> Simple Form </title>
        <link href="{self.css}" rel="Stylesheet" type="text/css" />
    </head>
    <body>'''
        page_body = '''<form method="GET">
            <label>Name:</label><input type="text" name="name" /><br/><br/>
            <label>Email:</label><input type="text" name="email" /><br/><br/>
            <label>Address:</label><input type="text" name="address" /><br/><br/>
            <label>Phone Number:</label><input type="text" name="phone" /><br/><br/>
            <label>Gender:
                <input type="radio" name="sex" value="male" checked>Male
                <input type="radio" name="sex" value="female">Female <br/><br/>
            </label>
            <label>Employment Status:
                <select name="status">
                    <option value="employed">Employed</option>
                    <option value="unemployed">Unemployed</option>
                    <option value="student">Student</option>
                    <option value="laid-off">Laid Off</option>
                </select><br/><br/>
            </label>
            <input type="submit" value="Submit" /> '''
        page_close = '''
        </form>
    </body>
</html>'''
