# -*- coding: utf-8 -*-

class Staff(object):
    # 员工信息类
    def __init__(
        self,
        num="",
        name="",
        gender="",
        score={1: 0, 2: 0, 3: 0, 4: 0},
        total=0,
        rank=0,
    ):
        self.__num = num  # 工号
        self.__name = name  # 姓名
        self.__gender = gender  # 性别
        self.__score = score  # 各季度业绩
        self.__total = total  # 总业绩
        self.__rank = rank  # 名次

    def getNum(self):
        return self.__num

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getScore(self):
        return self.__score

    def getTotal(self):
        return self.__total

    def getRank(self):
        return self.__rank

    def setName(self, name):
        self.__name = name

    def setGender(self, gender):
        self.__gender = gender

    def setScore(self, score):
        self.__score = score

    def setTotal(self, total):
        self.__total = total

    def setRank(self, rank):
        self.__rank = rank
