'''
Name: Allison Sharpe
Date: 10/7/15
Class: Design Patters for Web Programming
Assignment: Simple Form
'''

class Page(): #Class for Page()
    def __init__(self, page_main): #Instances set for class Page()
        self.css = "css/style.css" #CSS stylesheet for Page()
        self.head = '''<!DOCTYPE HTML> <!-- Head of the page -->
        <html>
            <head> <!-- Head tag -->
                <title>Sharpe's Inc. - Apply Today</title> <!-- Title for Sharpe's Inc./Sharpe's Inc. is a made up company -->
       			<link href="{self.css}" rel="stylesheet" type="text/css" /> <!-- Link to my stylesheet in the head tag -->
            </head>
            <body>
            '''
        self.body = ''' <!-- Body of the page -->
        		<form method="GET">
            		<h1> Sharpe's Inc. Application Form </h1> <!-- Main header for Sharpe's Inc. -->
            		<p> Fill out the form below to get started. </p> <!-- Paragraph displayed underneath header and above form -->
            		<label>Name:</label><input type="text" name="name" class="fields"/><br/><br/> <!-- Collects name from user -->
            		<label>Email:</label><input type="text" name="email" class="fields"/><br/><br/> <!-- Collects email from user -->
            		<label>Address:</label><input type="text" name="address" class="fields"/><br/><br/> <!-- Collects address from user -->
            		<label>Phone:</label><input type="text" name="phone" class="fields" /><br/><br/> <!-- Collects phone number from user -->
            		<label>Job Dept: <!-- Select options for the job department -->
                	<select name="dept">
                    	<option value="Headquarters">Headquarters</option>
                    	<option value="Distribution">Distribution Centers</option>
                	</select><br/><br/>
           	 		</label>
            		<label>Would you be willing to relocate if required? <!-- Radio option for relocation -->
                		<input type="radio" name="relocate" value="Yes" checked> Yes
                		<input type="radio" name="relocate" value="No" checked> No <br/><br/>
            		</label>
            		<input type="submit" id="submit" value="Submit"> <!-- Submit button for the form -->
            	</form>	'''
        self.close = ''' <!-- Footer of the page -->
            </body>
        </html>
        	'''

    def print_info(self, x=''): #Prints information to browser
        if x=='':
            all = self.head + self.body + self.close #Retrieves self.head, self.body, and self.close from the html
            all = all.format(**locals()) #Enables css
            return all #Returns variable all
        else:
            return self.head + x + self.close #Returns variables in order to print information to new browser

