# -*- coding: UTF-8 -*-
from Question import Question
from pypinyin import pinyin,lazy_pinyin
import Trie
import numpy

allQues = []

# 解析出来题目
def parse():
    num = 1
    findNum = 0
    with open("README.txt", encoding="utf-8") as r:
        line = r.readline()
        findFlag = False
        tmpQues = Question()
        letter = 'A'
        while line:
            if line.find(str(num) + "、") != -1 or line.find("出题") != -1:
                findNum = findNum + 1
                tmpQues.setNum(num)
                tmpQues.setTitle(line[(len(str(num)) + 1):] )
                findFlag = True
                # nowLine = line
                line = r.readline()
                continue
            if findFlag:
                # nowLine = nowLine + line
                if line.find(letter+'、') != -1:
                    tmpQues.addAnswerContent(line)
                    letter = chr(ord(letter)+1 )
                
            if line.find("答案") != -1:
                # dealOne(nowLine)      
                # nowLine = ""
                tmpQues.setAnswer(line.split()[0][-1]) # 设置答案
                allQues.append(tmpQues)
                tmpQues = Question()
                findFlag = False
                letter = "A"
                num = num + 1 # 一个题目解析完成
            line = r.readline()
# 解析出来的题目处理下，构建字典树
def init():
    for ques in allQues:
        zh = ques.getTitle()
        ques.setTips(zh)
        pin = lazy_pinyin(zh)
        spell = ""
        for i in pin:
            spell = spell + i[0] #加上首字母
        ques.setSpell(spell)
    # print(len(allQues))
    # print(allQues[0].getNum())
    # print(allQues[0].getSpell())
    for ques in allQues:
        Trie.addTrieOne(ques.getNum(), ques.getSpell())

# 解析函数，查询字典树实现传入字符串返回解析到的题目ID列表
def findBySpell(objStr):
    res = Trie.findQuesByTrie(objStr)
    return res

def test():
    num = 1
    findNum = 0
    with open("README.txt", encoding="utf-8") as r:
        line = r.readline()
        findFlag = False
        while line:
            if line.find(str(num) + "、") != -1:
                findNum = findNum + 1
                findFlag = True
                line = r.readline()
                continue
            if line.find("答案：") != -1:
                if findFlag == False:
                    print(num)
                    break
                findFlag = False
                num = num + 1 # 一个题目解析完成
            line = r.readline()
    print(num)
    # print(findNum)
if __name__ == "__main__":
    # test()
    parse()
    init()
    print(findBySpell("t"))
