'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

class Scores(object):
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.score4 = 0
        self.__final_score = 0

    @property
    def final_score(self):
        return self.__final_score

    @final_score.setter
    def final_score(self, new_final_score):
        self.__final_score = new_final_score

    def calc_score(self):
        #Calculate final grade
        self.__final_score = (self.score1 + self.score2 + self.score3 + self.score4 + self.final_score)/5