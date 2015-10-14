'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

from lib import Students, StudentData


class ResultsPage(object): #Class for ResultsPage if the user enters in data
    def __init__(self):
        self.title = "Student Evaluation"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title> Student Evaluation </title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.body = ""
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        return all


class FormPage(object): #Class for FormPage class if the user does not enter any data
    def __init__(self):
        self.title = "Welcome"
        self.css = "css/styles.css"
        self.head = """
                <!DOCTYPE HTML>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Student Evaluation</title>
		<link href="css/style.css" rel="Stylesheet" type="text/css">
	</head>
    <body>
        """
        self.body = """
			<header>
				<h1>Student Evaluation</h1>
				<p> Enter in student's information below. </p>
			</header>
			<form>
			    First Name: <input type="text" name="first"><br>
			    Last Name: <input type="text" name="last"><br>
			    Grade Level: <input type="text" name="level"><br>
			    GPA: <input type="text" name="gpa"><br>
				<input type="submit" value="Submit">
			</form>
        """
        self.__error = ''
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        return all