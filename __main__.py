from file import*
from staff import*

def printHead():
    #打印员工信息表头
    print('-'*30)
    print('工号\t姓名\t性别\t第一季度业绩\t第二季度业绩\t第三季度业绩\t第四季度业绩\t总业绩\t名次')

def menu():
    #顶层菜单函数
    print('-'*30)
    print('1.显示基本信息')
    print('2.基本信息管理')
    print('3.员工业绩管理')
    print('4.员工业绩统计')
    print('5.根据条件查询')
    print('0.退出')
    print('-'*30)

def menuShow():
    #1.数据展示菜单函数
    print('-'*30)
    print('1.按工号显示信息')
    print('2.按姓名显示信息')
    print('3.按总业绩显示信息')
    print('0.返回上层菜单')
    print('-'*30)

def menuBase():
    #2.基本信息管理菜单函数
    print('-'*30)
    print('1.插入员工记录')
    print('2.删除员工记录')
    print('3.修改员工记录')
    print('0.返回上层菜单')
    print('-'*30)

def menuScore():
    #3.员工业绩管理菜单函数
    print('-'*30)
    print('1.计算员工总业绩')
    print('2.根据总业绩排名')
    print('0.返回上层菜单')
    print('-'*30)

def menuCount():
    #4.员工业绩统计菜单函数
    print('-'*30)
    print('1.求业绩最高值')
    print('2.求业绩最低值')
    print('3.求业绩平均分')
    print('0.返回上层菜单')
    print('-'*30)

def menuSearch():
    #5.根据条件查询菜单函数
    print('-'*30)
    print('1.按工号查询')
    print('2.按姓名查询')
    print('3.按名次查询')
    print('0.返回上层菜单')
    print('-'*30)

def showManage():
    global staList
    #该函数完成数据展示功能，提示用户按照工号，姓名，总业绩排名展示数据
    while True:
        menuShow()
        choice=input("请输入您的选择(0-3):")
        if choice=='1':
            sortSta(staList,"工号")
        elif choice=='2':
            sortSta(staList,"姓名")
        elif choice=='3':
            sortSta(staList,"总业绩")
            staList=staList[::-1]
        else:
            break
        printHead()
        printSta(staList)

def baseManage():                    
    #该函数完成基本信息管理，按工号进行插入删除修改，工号不能重复
    while True:                          #按工号进行插入删除修改，工号不能重复
        menuBase()                       #显示对应的二级菜单
        choice=input("请输入您的选择（0-3）：")
        if choice=='1':
            readSta(staList,1)         #读入一条待插入的员工记录
        elif choice=='2':
            num=input("请输入需要删除的员工工号：")
            deleteSta(staList,num)          #调用函数删除指定工号的员工记录
        elif choice=='3':
            num=input("请输入需要修改的员工工号：")
            found=searchSta(staList,num,"工号")
                                                   #调用函数查找指定工号的员工记录
            if found!=[]:                   #如果该工号的记录存在
                newSta=[]
                readSta(newSta,1)             #读入一条完整的员工记录信息
                staList[found[0]]=newSta[0]            #将刚读入的记录赋值给需要修改的员工记录
            else:
                print("该员工不存在，无法修改其信息！")
        else:   
            break

def scoreManage():
    #该函数完成员工业绩管理功能
    while True:
        menuScore()                    #显示对应的二级菜单
        choice=input("请输入您的选择（0-2）：")
        if choice=='1':
            for sta in staList:
                sta.calcTotal()
            print("计算所有员工总业绩完毕！")
        elif choice=='2':
            scores=[sta.getTotal() for sta in staList]
            for sta in staList:
                sta.calcRank(scores)
            print("计算所有员工排名完毕！")
        else:
            break
            
def countManage():
    #该函数完成员工工资统计功能
    while True:
        menuCount()                      #显示对应的二级菜单
        choice=input("请输入您的选择（0-3）：")
        if choice=='1':
            print("各季度业绩最高的员工分别是：")
            print("第一季度业绩：",max(staList,key=lambda sta:sta.getScore()["第一季度业绩"]))
            print("第二季度业绩：",max(staList,key=lambda sta:sta.getScore()["第二季度业绩"]))
            print("第三季度业绩：",max(staList,key=lambda sta:sta.getScore()["第三季度业绩"]))
            print("第四季度业绩：",max(staList,key=lambda sta:sta.getScore()["第四季度业绩"]))
        elif choice=='2':
            print("各季度业绩最低的员工分别是：")
            print("第一季度业绩：",min(staList,key=lambda sta:sta.getScore()["第一季度业绩"]))
            print("第二季度业绩：",min(staList,key=lambda sta:sta.getScore()["第二季度业绩"]))
            print("第三季度业绩：",min(staList,key=lambda sta:sta.getScore()["第三季度业绩"]))
            print("第四季度业绩：",min(staList,key=lambda sta:sta.getScore()["第四季度业绩"]))
        elif choice=='3':
            print("各季度业绩的平均值：")
            print("第一季度业绩：",sum([sta.getScore()["第一季度业绩"] for sta in staList])/len(staList))
            print("第二季度业绩：",sum([sta.getScore()["第二季度业绩"] for sta in staList])/len(staList))
            print("第三季度业绩：",sum([sta.getScore()["第三季度业绩"] for sta in staList])/len(staList))
            print("第四季度业绩：",sum([sta.getScore()["第四季度业绩"] for sta in staList])/len(staList))
        else:
            break
    
def searchManage():
    #该函数完成根据条件查询功能
    while True:
        menuSearch()                     #显示对应二级菜单
        choice=input("请输入您的选择（0-3）：")
        if choice=='1':
            keyword,condition=input("请输入待查询员工的工号："),"工号"
        elif choice=='2':
            keyword,condition=input("请输入待查询员工的姓名："),"姓名"                
        elif choice=='3':
            keyword,condition=int(input("请输入待查询员工的名次：")),"排名"
        else:
            break
        found=searchSta(staList,keyword,condition)
                                                       #查找的符合条件元素的下标存于f列表中
        if found:                        #如果查找成功
            printHead()                       #打印表态
            for i in found:                      #循环控制f列表的下标
                print(staList[i])                   #每次输出一条记录
        else:
            print("查找的记录不存在")               #如果查找不到元素，则输出提示信息

def runMain(choice):
    #主控模板，对应于下一级菜单其下各功能选择执行
    if choice=='1':
        showManage()                      #1.显示基本信息
    elif choice=='2':
        baseManage()                     #2.基本信息管理
    elif choice=='3':
        scoreManage()                    #3.员工业绩管理
    elif choice=='4':
        countManage()                    #4.员工业绩统计
    elif choice=='5':
        searchManage()                   #5.根据条件查询

if __name__=="__main__":
    staList=[]                   #定义实参一维列表存储员工记录
    n=readFile(staList)       #首先读取文件，记录条数返回赋值给n
    if n == 0:                  #如果原来文件为空
        n=createFile(staList)            #则首先要建立文件，从键盘上读入一系列记录存于文件
    print('-'*30)
    print('欢迎您使用企业员工业绩管理系统')
    while True:
        menu()                           #显示主菜单
        choice = input("请输入您的选择（0-5）：")
        if choice=='0':
            print("感谢您的使用，再见！")
            saveFile(staList)
            break                        #退出循环，停止接收用户的输入
        elif choice>'0' and choice<='5':
            runMain(choice)              #通过调用此函数进行一级功能项的选择执行
        else:
            print("输入错误，请重新输入！")
