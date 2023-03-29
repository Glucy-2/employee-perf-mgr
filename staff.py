class Staff(object):
    #员工信息类
    def __init__(self,num='',name='',gender='',score={"第一季度业绩":0,"第二季度业绩":0,"第三季度业绩":0,"第四季度业绩":0},total=0,rank=0):
        self.__num=num           #工号
        self.__name=name        #姓名
        self.__gender=gender    #性别
        self.__score=score       #各季度业绩
        self.__total=total           #总业绩
        self.__rank=rank            #名次

    def __str__(self):
        s="{:<12}{:<12}{:<10}{:<12}{:<12}{:<12}{:<12}{:<12}{:<8}".format(
            self.__num,self.__name,self.__gender,
            self.__score["第一季度业绩"],self.__score["第二季度业绩"],self.__score["第三季度业绩"],self.__score["第四季度业绩"],
            self.__total,self.__rank)
        return s
    
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

    def calcTotal(self):
        self.__total=sum(self.__score.values())

    def calcRank(self,scores):
        count=1
        for score in scores:
            if score>self.__total:
                count+=1
        self.__rank=count

def readSta(staList,n=20):
    #读入员工记录值，工号为0或读满规定条数记录时停止
    while n>0:
        print("请输入一个员工的详细信息（工号为0时结束输入）：")
        num=input("工号：")            #输入工号
        if num == '0':                        #工号为0停止输入
            break
        else:
            if searchSta(staList,num,"工号")!=[]:
                                               #工号相同不允许插入，保证工号的唯一性
                print("列表中存在相同的工号，禁止插入！")
                return len(staList)
            name= input("姓名：")          #输入名字
            gender = input("性别：")       #输入性别
            score = {}                          #创建空字典用于存放员工的业绩
            print("请输入该员工的各季度业绩，用空格分隔：")
            score["第一季度业绩"],score["第二季度业绩"],score["第三季度业绩"],score["第四季度业绩"] = map(float,input( ).split())
            oneSta=Staff(num,name,gender,score)
            staList.append(oneSta)
            n=n-1
    return len(staList)          #返回实际读入的记录条数

def printSta(staList):
    #输出所有员工记录的值
    for sta in staList:
        print(sta)
        
def searchSta(staList,keyword,condition):
    result=[]
    for i in range(len(staList)):
        if condition == "工号" and staList[i].getNum() == keyword:
            result.append(i)
        elif condition == "姓名" and staList[i].getName()== keyword:
            result.append(i)
        elif condition == "排名" and staList[i].getRank()== int(keyword):
            result.append(i)
        elif condition == "总业绩" and staList[i].getTotal()==float(keyword):
            result.append(i)
    return result

def deleteSta(staList,num):         #从列表中删除指定工号的一个元素
    for sta in staList:             #寻找待删除的元素
        if sta.getNum()==num:                #如果找到相等元素
            staList.remove(sta)                     #删除对应的元素
            print("已删除指定工号的员工信息")
            break
    else:                              #如果找不到待删除的元素
        print("该员工不存在，删除失败!")                   #给出提示信息后返回

def compare(s1,s2,condition):
    #根据condition条件比较两个staff记录的大小
    if condition=="工号":
        return s1.getNum()>s2.getNum()
    if condition=="姓名":
        return s1.getName()>s2.getName()
    if condition=="总业绩":
        return s1.getTotal()>s2.getTotal()

def sortSta(staList,condition):         #选择法排序，按condiion条件由小到大排序
    for i in range(0,len(staList)-1):           #控制循环的n-1次
        minpos=i             #minpos用来存储本次循环的最小元素所在下标
        for j in range(i+1,len(staList)):     #寻找本次循环的最小元素所在的下标
            if compare(staList[minpos],staList[j],condition):
                minpos=j
        if i!=minpos:           #保证本次循环的最小元素到达下标为i的位置
            staList[i],staList[minpos]=staList[minpos],staList[i]
