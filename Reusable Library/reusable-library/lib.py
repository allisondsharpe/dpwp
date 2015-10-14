'''
Name: Allison Sharpe
Date: 10-12-15
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''


class Students(object): #Class for Students
    def __init__(self):
        self.__first = ''
        self.__last = ''
        self.__level = 0
        self.__gpa = 0

    #Getters
    @property
    def first_name(self):
        return self.__first

    @property
    def last_name(self):
        return self.__last

    @property
    def grade_level(self):
        return self.__level

    @property
    def gpa(self):
        return self.__gpa


    #Setters
    @first_name.setter
    def first_name(self, rp_first):
        self.__first = rp_first

    @last_name.setter
    def last_name(self, rp_last):
       self.__score2 = rp_last

    @grade_level.setter
    def grade_level(self, rp_level):
        self.__level = rp_level

    @gpa.setter
    def gpa(self, rp_gpa):
       self.__score4 = rp_gpa


class StudentData(object): #Class for StudentData
    def __init__(self):
        pass