'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

class ResultsPage(object): #Class for ResultsPage()
    def __init__(self):
        self.__title = "The Score Board" #Private attribute for self.__title
        self.css = "css/style.css" #Attribute for self.css
        self.__head = """ <!-- Private attribute for self.__head -->
<!DOCTYPE HTML>
<html>
	<head> <!-- Head tag created to store title and css stylesheet link -->
		<title> The Score Board </title>
		<link href="css/style.css" rel="stylesheet" type="text/css">
	</head>
    <body>
		<header> <!-- Header tag created to store main h1 and paragraph tag -->
			<h1> Arcade Gaming Score Board</h1>
			<p> Below are five individual people competing for top scores. </p>
		</header>
        """
        self.body = """ <!Enables the form to be printed out to the browser -->

        <script src="js/main.js></script> """ #Javascript file used to validate form fields

        self.close = """ <!-- Stores the closing body and html tags/Footer -->
    </body>
</html>
        """

    def print_out(self): #Prints information to browser
        all = self.__head + self.body + self.close #Retrieves self.head, self.body, and self.close from the html
        return all #Returns variable all


class FormPage(object): #Class for FormPage()
    def __init__(self):
        self.__title = "The Score Board"
        self.css = "css/style.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title> The Score Board </title>
		<link href="css/style.css" rel="stylesheet" type="text/css">
	</head>
    <body>
        """
        self.body = """
			<header>
				<h1>Arcade Gaming Score Board</h1>
				<p>Enter in five individuals to compete for the highest score.</p>
			</header>
			<form name="myForm" onsubmit="return validateForm()">
				<h2> 1st Competitor </h2>
				<label>Name:
					<input type="text" name="s1_name"></br>
				</label>
				<label>Score #1:
					<input type="text" name="s1_score1"></br>
				</label>
				<label>Score #2:
					<input type="text" name="s1_score2"></br>
				</label>
				<label>Score #3:
					<input type="text" name="s1_score3"></br>
				</label>
				<label>Score #4:
					<input type="text" name="s1_score4"></br>
				</label>
				<label>Final Score:
					<input type="text" name="s1_final"></br>
				</label>

				<h2> 2nd Competitor  </h2>
				<label>Name:
					<input type="text" name="s2_name"></br>
				</label>
				<label>Score #1:
					<input type="text" name="s2_score1"></br>
				</label>
				<label>Score #2:
					<input type="text" name="s2_score2"></br>
				</label>
				<label>Score #3:
					<input type="text" name="s2_score3"></br>
				</label>
				<label>Score #4:
					<input type="text" name="s2_score4"></br>
				</label>
				<label>Final Score:
					<input type="text" name="s2_final"></br>
				</label>

				<h2> 3rd Competitor </h2>
				<label>Name:
					<input type="text" name="s3_name"></br>
				</label>
				<label>Score #1:
					<input type="text" name="s3_score1"></br>
				</label>
				<label>Score #2:
					<input type="text" name="s3_score2"></br>
				</label>
				<label>Score #3:
					<input type="text" name="s3_score3"></br>
				</label>
				<label>Score #4:
					<input type="text" name="s3_score4"></br>
				</label>
				<label>Final Score:
					<input type="text" name="s3_final"></br>
				</label>

				<h2> 4th Competitor </h2>
				<label>Name:
					<input type="text" name="s4_name"></br>
				</label>
				<label>Score #1:
					<input type="text" name="s4_score1"></br>
				</label>
				<label>Score #2:
					<input type="text" name="s4_score2"></br>
				</label>
				<label>Score #3:
					<input type="text" name="s4_score3"></br>
				</label>
				<label>Score #4:
					<input type="text" name="s4_score4"></br>
				</label>
				<label>Final Score:
					<input type="text" name="s4_final"></br>
				</label>

				<h2> 5th Competitor </h2>
				<label>Name:
					<input type="text" name="s5_name"></br>
				</label>
				<label>Score #1:
					<input type="text" name="s5_score1"></br>
				</label>
				<label>Score #2:
					<input type="text" name="s5_score2"></br>
				</label>
				<label>Score #3:
					<input type="text" name="s5_score3"></br>
				</label>
				<label>Score #4:
					<input type="text" name="s5_score4"></br>
				</label>
				<label>Final Score:
					<input type="text" name="s5_final"></br>
				</label>

				<input type="submit" id="submit" value="Submit">
			</form>

			<script src="js/main.js></script> <!-- Javascript file used to validate form fields -->
	"""
        self.close = """
    </body>
</html>
        """
    def print_out(self): #Prints information to browser
        all = self.__head + self.body + self.close #Retrieves self.head, self.body, and self.close from the html
        all = all.format(**locals()) #Enables css
        return all #Returns variable all
