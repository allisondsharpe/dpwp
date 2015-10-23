'''
Name: Allison Sharpe
Date: 10-17-15
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

class Lib(object): #Class created for Scores() - Stores data for form inputs
    def __init__(self):
        self.__name = '' #Stores string value for __name attribute

    '''
    GETTERS
    '''

    #Name getter used to retrieve value of __name
    @property
    def name(self):
        return self.__name


    '''
    SETTERS
    '''

    #Name setter used to retrieve and modify value of __name
    @name.setter
    def name(self, rp_name):
        self.__name = rp_name



class LibData(object): #Class created for ScoreData()
    def __init__(self):
        self.__score_list = [] #Array created for each competitor's scores

    def add_new_competitor(self, rp): #Function for add_new_competitor created from main.py
        self.__score_list.append(rp)
        print rp.name #Adds new competitor to the score_list, then prints the name of each competitor

    def calc_score1(self): #Function for calc_score1
        output = '' #Variable "output" created in order to print the results to the browser
        for competitor in self.__score_list:
            output += "Competitor " + str(competitor.name) + " got a total of " + str(competitor.score1) + " points for the first round." + "<br />" #Prints the competitor's name and score to the browser using the output variable
        return output #Returns variable output so that it will run in the browser

