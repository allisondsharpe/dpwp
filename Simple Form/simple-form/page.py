'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

class Page(): #class for Page()
    def __init__(self, page_main): #instances set for class Page()
        self.css = "css/style.css" #css stylesheet
        self.head = '''<!DOCTYPE HTML> <!-- inserts html -->
        <html>
            <head> <!-- header tag -->
                <title>Sharpe's Inc. - Apply Today</title> <!-- Sharpe's Inc. is a made up company -->
       			<link href="{self.css}" rel="stylesheet" type="text/css" /> <!-- link to my stylesheet -->
            </head>
            <body>
            '''
        self.body = '''
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
            		<a href="../new-page.py"><input type="submit" id="submit" value="Submit"></a> <!-- submit button for form -->
            	</form>	'''
        self.close = '''
            </body>
        </html>
        	'''

    def print_info(self, i=''):
        if i=='':
            return self.head + self.body + self.close
        else:
            return self.head + i + self.close

