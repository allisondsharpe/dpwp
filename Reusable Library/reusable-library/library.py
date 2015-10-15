'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

class Scores(object):
    def __init__(self):
        self.__name = ''
        self.__score1 = 0
        self.__score2 = 0
        self.__score3 = 0
        self.__score4 = 0
        self.__final = 0

    #Name getter
    @property
    def name(self):
        return self.__name

    #Name setter
    @name.setter
    def name(self, rp_name):
        self.__name = rp_name

    #Score 1 getter
    @property
    def score1(self):
        return self.__score1

    #Score 1 setter
    @score1.setter
    def score1(self, rp_score1):
        self.__score1 = rp_score1

    #Score 2 getter
    @property
    def score2(self):
        return self.__score2

    #Score 2 setter
    @score2.setter
    def score2(self, rp_score2):
        self.__score2 = rp_score2

    #Score 3 getter
    @property
    def score2(self):
        return self.__score2

    #Score 3 setter
    @score2.setter
    def score2(self, rp_score2):
        self.__score2 = rp_score2

    #Score 4 getter
    @property
    def score4(self):
        return self.__score4

    #Score 4 setter
    @score4.setter
    def score4(self, rp_score4):
        self.__score4 = rp_score4

    #Final score getter
    @property
    def final(self):
        return self.__final

    #Final score setter
    @final.setter
    def final(self, rp_final):
        self.__final = rp_final


class ScoreData(object):
    def __init__(self):
        self.__score_list = [] #Array for list of scores

    def add_new_competitor(self, rp):
        self.__score_list.append(rp)
        print rp.name

    def calc_score1(self):
        output = ''
        for competitor in self.__score_list:
            output += "Competitor got a total of " + str(competitor.score1) + " for the first round." + "<br />"
        return output

    def calc_score2(self):
        output = ''
        for competitor in self.__score_list:
            output += "Competitor got a total of " + str(competitor.score2) + " for the second round." + "<br />"
        return output

    def calc_score3(self):
        output = ''
        for competitor in self.__score_list:
            output += "Competitor got a total of " + str(competitor.score3) + " for the third round." + "<br />"
        return output

    def calc_score4(self):
        output = ''
        for competitor in self.__score_list:
            output += "Competitor got a total of " + str(competitor.score4) + " for the fourth round." + "<br />"
        return output

    def calc_final(self):
        '''
        calculate final score
        '''
        #score
        score = []
        for competitor in self.__score_list:
            score.append(competitor.year)

        print score
        #sort score from low to high
        score.sort()
        print score
        #subtract the low score from the high score
        num = len(score) - 1 #length of array
        span = score[num] - score[0] #last number - first number
        #return the span of time
        return "The span between scores entered is " + str(span)

