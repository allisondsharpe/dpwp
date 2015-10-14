'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

from lib import Scores, ScoreData


class ResultsPage(object): #class for ResultsPage if the user enters in data
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title> Final Scores! </title>
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


class FormPage(object): #form page class for if the user does not enter any data
    def __init__(self):
        self.title = "Welcome"
        self.css = "css/styles.css"
        self.head = """
                <!DOCTYPE HTML>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Team Stats Calculator</title>
		<link href="css/styles.css" rel="Stylesheet" type="text/css">
		<link href='http://fonts.googleapis.com/css?family=Permanent+Marker' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Quicksand:400,700' rel='stylesheet' type='text/css'>
	</head>
    <body>
        """
        self.body = """
			<header>
				<h1>Welcome!</h1>
				<p> Enter in your information down below! </p>
			</header>
			<form>
			    Name: <input type="text" name="name"><br>
			    Date: <input type="text" name="date"><br>
			    Address: <input type="text" name="address"><br>
			    Phone: <input type="text" name="phone"><br>
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