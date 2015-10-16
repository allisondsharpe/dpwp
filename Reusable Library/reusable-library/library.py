'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

class Scores(object): #Class created for Scores() - Stores data for form inputs
    def __init__(self):
        self.__name = '' #Stores string value for __name attribute
        self.__score1 = 0 #Stores number value for __score1 attribute
        self.__score2 = 0 #Stores number value for __score2 attribute
        self.__score3 = 0 #Stores number value for __score3 attribute
        self.__score4 = 0 #Stores number value for __score4 attribute
        self.__final = 0 #Stores number value for __score1 attribute

    '''
    GETTERS
    '''

    #Name getter used to retrieve value of __name
    @property
    def name(self):
        return self.__name

   #Score 1 getter used to retrieve value of __score1
    @property
    def score1(self):
        return self.__score1

    #Score 2 getter used to retrieve value of __score2
    @property
    def score2(self):
        return self.__score2

    #Score 3 getter used to retrieve value of __score3
    @property
    def score3(self):
        return self.__score3

    #Score 4 getter used to retrieve value of __score4
    @property
    def score4(self):
        return self.__score4

    #Final Score getter used to retrieve value of __final
    @property
    def final(self):
        return self.__final

    '''
    SETTERS
    '''

    #Name setter used to retrieve and modify value of __name
    @name.setter
    def name(self, rp_name):
        self.__name = rp_name

    #Score 1 setter used to retrieve and modify value of __score1
    @score1.setter
    def score1(self, rp_score1):
        self.__score1 = rp_score1

    #Score 2 setter used to retrieve and modify value of __score2
    @score2.setter
    def score2(self, rp_score2):
        self.__score2 = rp_score2

    #Score 3 setter used to retrieve and modify value of __score3
    @score3.setter
    def score3(self, rp_score3):
        self.__score3 = rp_score3

    #Score 4 setter used to retrieve and modify value of __score4
    @score4.setter
    def score4(self, rp_score4):
        self.__score4 = rp_score4

    #Score 4 setter used to retrieve and modify value of __score4
    @final.setter
    def final(self, rp_final):
        self.__final = rp_final


class ScoreData(object): #Class created for ScoreData()
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

    def calc_score2(self): #Function for calc_score2
        output = '' #Variable "output" created in order to print the results to the browser
        for competitor in self.__score_list:
            output += "Competitor " + str(competitor.name) + " got a total of " + str(competitor.score2) + " points for the second round." + "<br />" #Prints the competitor's name and score to the browser using the output variable
        return output #Returns variable output so that it will run in the browser

    def calc_score3(self): #Function for calc_score3
        output = '' #Variable "output" created in order to print the results to the browser
        for competitor in self.__score_list:
            output += "Competitor " + str(competitor.name) + " got a total of " + str(competitor.score3) + " points for the third round." + "<br />" #Prints the competitor's name and score to the browser using the output variable
        return output #Returns variable output so that it will run in the browser

    def calc_score4(self): #Function for calc_score1
        output = '' #Variable "output" created in order to print the results to the browser
        for competitor in self.__score_list:
            output += "Competitor " + str(competitor.name) + " got a total of " + str(competitor.score4) + " points for the fourth round." + "<br />" #Prints the competitor's name and score to the browser using the output variable
        return output #Returns variable output so that it will run in the browser




