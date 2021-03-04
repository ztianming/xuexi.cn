# -*- coding: UTF-8 -*-

class Question:
    def __init__(self):
        self._answer = ""  # 答案分 A/B/C/D/...
        self._answerContent = [] # ABCD对应内容列表
        self._title = "" # 题目描述    
        self._spell = "" # 英文拼写检索
        self._number = -1 # 题目序号
        self._tips = ""  # 搜索时提示的中文题目
    
    # def __init__(self, number, answer, answerContent, title):
    #     self._answer = answer  # 答案分 A/B/C/D/...
    #     self._answerContent = answerContent # ABCD对应内容列表
    #     self._title = title # 题目描述
    #     self._spell = "" # 英文拼写检索
    #     self._number = -1 # 题目序号
    #     self._tips = ""  # 搜索时提示的中文题目
        
    def setAnswer(self, answer):
        self._answer = answer
    def setNum(self, num):
        self._number = num
    def addAnswerContent(self, option):
        self._answerContent.append(option)
    def setTitle(self, title):
        self._title = title
    def setTips(self, tips):
        self._tips = tips
    def setSpell(self, spell):
        self._spell = spell
    def getTitle(self):
        return self._title
    def getNum(self):
        return self._number
    def getSpell(self):
        return self._spell