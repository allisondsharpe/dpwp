class Page():

    def __init__(self, main):
        self.head = '''<!DOCTYPE HTML>
        <html>
            <head>
                <title>Simple Form</title>
                <link href="style.css" type="text/css" rel="stylesheet" />
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
                    <option value="Headquarters">Headquarters</option>
                    <option value="Distribution">Distribution Centers</option>
                </select><br/><br/>
            </label>
            <label>Would you be willing to relocate if required? <!-- radio option for relocation -->
                <input type="radio" name="relocate" value="Yes" checked> Yes
                <input type="radio" name="relocate" value="No" checked> No <br/><br/>
            </label>
            <a href="../new-page.py"><input type="submit" id="submit" value="Submit"></a> <!-- submit button for form -->
        '''

        self.close = '''
            </body>
        </html>
            '''

        #main_self is SCOPED to __init__
        main.response.write("blablabablal")

    def print_contents(self, i=''):
        if i=='':
            return self.head + self.body + self.close + self.ender
        else:
            return self.head + i + self.close

class Button():
    def __init__(self):
        self.label = "Contact"
        self.size = 100
