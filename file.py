from staff import*

#sta为存储staff类的对象的列表
def createFile(staList):              #建立初始的数据文件
        print("请初始化员工数据")
        print("-"*30)
        readSta(staList)                       #调用staff.py中的函数读入数据
        saveFile(staList)
        return len(staList)
    
def readFile(staList):                           #将文件的内容读出置于对象列表sta中
    try:
        with open('staff.txt','r',encoding="UTF-8") as file:
            for line in file.readlines():
                if line!="":
                    s=line.rstrip('\n').split('\t')
                    num,name,gender=s[0],s[1],s[2]
                    score={"第一季度业绩":int(s[3]),"第二季度业绩":int(s[4]),"第三季度业绩":int(s[5]),"第四季度业绩":int(s[6])}
                    total,rank=int(s[7]),int(s[8])
                    oneSta= Staff(num,name,gender,score,total,rank)
                    staList.append(oneSta)
            return len(staList)      #返回记录条数
    except FileNotFoundError:
        print("数据文件不存在！")           #若打开失败，输入提示信息
        return 0                    #因为数据文件不存在，返回0，表述无员工数据

def saveFile(staList):
    try:
        with open('staff.txt','w',encoding="UTF-8") as file:
            tab='\t'
            for oneSta in staList:
                s=oneSta.getNum()+tab+oneSta.getName()+tab+oneSta.getGender()+tab+\
                   str(oneSta.getScore()['第一季度业绩'])+tab+str(oneSta.getScore()['第二季度业绩'])+tab+str(oneSta.getScore()['第三季度业绩'])+\
                   tab+str(oneSta.getScore()['第四季度业绩'])+tab+str(oneSta.getTotal())+tab+str(oneSta.getRank())+'\n'
                file.write(s)
    except IOError:
        print("文件打开错误！")             #如果打开失败，输出信息
        exit(0)                      #然后退出
