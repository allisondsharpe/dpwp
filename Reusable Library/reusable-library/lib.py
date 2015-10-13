'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

class Scores(object):
    def __init__(self):
        self.__score1 = 0
        self.__score2 = 0
        self.__score3 = 0
        self.__score4 = 0
        self.__final_score = 0

    #Getters
    @property
    def score_1(self):
        return self.__score1

    @property
    def score_2(self):
        return self.__score2

    @property
    def score_3(self):
        return self.__score3

    @property
    def score_4(self):
        return self.__score4

    @property
    def final_score(self):
        return self.__final_score

    #Setters
    @score_1.setter
    def score_1(self, new_final_score):
        self.__score1 = new_final_score

    @score_2.setter
    def score_2(self, new_final_score):
       self.__score2 = new_final_score

    @score_3.setter
    def score_3(self, new_final_score):
        self.__score3 = new_final_score

    @score_4.setter
    def score_4(self, new_final_score):
       self.__score4 = new_final_score

    @final_score.setter
    def final_score(self, new_final_score):
        self.__final_score = new_final_score

    def calc_score(self):
        #Calculate final grade
        self.__final_score = (self.__score1 + self.__score2 + self.__score3 + self.__score4 + self.final_score)/5