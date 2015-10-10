'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

class Page(): #class for Page()
    def __init__(self, page_main): #instances set for class Page()
        self.css = "css/style.css" #css stylesheet
        self.head = '''<!DOCTYPE HTML> <!-- self.head/html insertion -->
        <html>
            <head> <!-- header tag -->
                <title>Sharpe's Inc. - Apply Today</title> <!-- Sharpe's Inc. is a made up company -->
       			<link href="{self.css}" rel="stylesheet" type="text/css" /> <!-- link to my stylesheet -->
            </head>
            <body>
            '''
        self.body = ''' <!-- self.body -->
        		<form method="GET">
            		<h1> Sharpe's Inc. Application Form </h1> <!-- main header -->
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
            		<input type="submit" id="submit" value="Submit"> <!-- submit button for form -->
            	</form>	'''
        self.close = ''' <!-- self.close -->
            </body>
        </html>
        	'''

    def print_info(self, i=''): #prints information to browser
        if i=='':
            all = self.head + self.body + self.close #retrieves self.head, self.body, and self.close from html
            all = all.format(**locals()) #enables css
            return all #returns variable all

        else:
            return self.head + i + self.close #returns variables in order to print information to new browser

