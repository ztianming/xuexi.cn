# -*- coding: UTF-8 -*-
import queue

class TrieNode:
    def __init__(self):
        self.end = [] # 以此结束的题目序号列表
        self.char = "" # 自己代表的字符
        self.pointers = [] # 指向的节点
        self.pointerLabels = [] # 指向的字符标签

rootNode = TrieNode()
# 根据字符串数据构建Trie树
def createTrie(strlist):
    for str in strlist:
        cur = rootNode
        for i in range(str):
            ch = str[i]
            if ch not in cur.pointerLabels:
                # 添加新节点
                cur.pointerLabels.append(ch)
                newNode = TrieNode()
                newNode.char = ch
                cur.pointers.append(newNode)
                # if i != len(str)-1:
                cur = newNode
            else: # 说明在下面找到了
                pos = cur.pointerLabels.index(ch)
                cur = cur.pointers[pos]
        cur.end.append(-1) # 添加序号

def addTrieOne(num, str):
    cur = rootNode
    for i in range(len(str)):
        ch = str[i]
        if ch not in cur.pointerLabels:
            # 添加新节点
            cur.pointerLabels.append(ch)
            newNode = TrieNode()
            newNode.char = ch
            cur.pointers.append(newNode)
            # if i != len(str)-1:
            cur = newNode
        else: # 说明在下面找到了
            pos = cur.pointerLabels.index(ch)
            cur = cur.pointers[pos]
    cur.end.append(num) # 添加题目序号

def findQuesByTrie(x):
    cur = rootNode
    for i in range(len(x)):
        ch = x[i]
        if ch not in cur.pointerLabels:
            return []
        else:
            pos = cur.pointerLabels.index(ch)
            cur = cur.pointers[pos]
    # 找到cur之后往下面遍历一下把所有对应的序号都输出一下就可以了
    res = []
    nodeQue = queue.Queue()
    nodeQue.put(cur)
    while nodeQue.qsize() != 0:
        topnode = nodeQue.get()
        for i in topnode.end:
            res.append(i)
        for i in topnode.pointers:
            nodeQue.put(i)
    return res


if __name__ == "__main__":
    pass