from ast import keyword
from Ui_Main import Ui_MainForm
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QCoreApplication, Qt
from staff import Staff,printSta
from ModifyForm import ModifyForm
from CreateForm import CreateForm

class MainForm(QWidget,Ui_MainForm):
    
    def __init__(self,*args,**kwargs):
        super(MainForm,self).__init__(*args,**kwargs)
        self.setupUi(self)

        #员工信息表用的模型
        self.staffmsg = QStandardItemModel()
        #暂存员工信息的list
        self.stafflist = []
        self.load_data()
        
        self.createform = CreateForm()
        self.modifyform = ModifyForm()
        self.createform.confirm_create_signal.connect(self.createAction)
        self.modifyform.confirm_modify_signal.connect(self.modifyAction)
        
        self.tableStaff.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableSearch.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.btnDelStaff.clicked.connect(self.deleteStaff)
        self.btnAlterStaff.clicked.connect(self.modifyStaff)
        self.btnAddStaff.clicked.connect(self.createStaff)
        self.btnSearch.clicked.connect(self.search)
        self.boxSort.currentIndexChanged.connect(self.changeSort)
        self.btnSearchSalary.clicked.connect(self.sortSalary)
        
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        
        self.averageSalary()
        
    def show_win(self):
        self.show()
        
    def load_data(self):
        #读取文件并且绑定到程序中
        tmp_list = ['工号','姓名','性别','岗位','基本工资','奖金','总工资']
        for i in range(len(tmp_list)):
            self.staffmsg.setHorizontalHeaderItem(i,QStandardItem(tmp_list[i]))
        for i in range(self.readFile(self.stafflist)):
            self.staffmsg.setItem(i,0,QStandardItem(self.stafflist[i].getNum()))
            self.staffmsg.setItem(i,1,QStandardItem(self.stafflist[i].getName()))
            self.staffmsg.setItem(i,2,QStandardItem(self.stafflist[i].getGender()))
            self.staffmsg.setItem(i,3,QStandardItem(self.stafflist[i].getPost()))
            self.staffmsg.setItem(i,4,QStandardItem(str(self.stafflist[i].getScore()['基本工资'])))
            self.staffmsg.setItem(i,5,QStandardItem(str(self.stafflist[i].getScore()['奖金'])))
            self.staffmsg.setItem(i,6,QStandardItem(str(self.stafflist[i].getTotal())))
        
        #按照编号进行排列
        self.staffmsg.sort(0,QtCore.Qt.AscendingOrder)
        #绑定模型
        self.tableStaff.setModel(self.staffmsg)
        
    def readFile(self,staList):                           #将文件的内容读出置于对象列表sta中
        try:
            with open('staff.txt','r',encoding="UTF-8") as file:
                for line in file.readlines():
                    if line!="":
                        s=line.rstrip('\n').split('\t')
                        num,name,gender,post=s[0],s[1],s[2],s[3]
                        score={"基本工资":float(s[4]),"奖金":float(s[5])}
                        total,rank=float(s[6]),int(s[7])
                        oneSta= Staff(num,name,gender,post,score,total,rank)
                        staList.append(oneSta)
                return len(staList)      #返回记录条数
        except FileNotFoundError:
            QMessageBox.warning(self,"警告","数据文件不存在！")
            return 0
    
    def changeSort(self):
        if self.boxSort.currentText()=='工号':
            self.staffmsg.sort(0,QtCore.Qt.AscendingOrder)
        elif self.boxSort.currentText()=='姓名':
            self.staffmsg.sort(1,QtCore.Qt.AscendingOrder)
        else:
            self.staffmsg.sort(6,QtCore.Qt.DescendingOrder)
    
    def deleteStaff(self):
        reply = QMessageBox.information(self,'提示','是否要删除员工： '+self.staffmsg.item(self.tableStaff.currentIndex().row(),0).text(),QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            r = self.tableStaff.currentIndex().row()
            self.staffmsg.removeRow(r)
            #print(self.staffmsg.itemData(self.staffmsg))
    
    def createStaff(self):
        for i in range(self.staffmsg.rowCount()):
            self.createform.num_list.append(self.staffmsg.item(i,0).text())
        self.createform.show()
        
    def modifyStaff(self):
        for i in range(self.staffmsg.rowCount()):
            if i==self.tableStaff.currentIndex().row():
                continue
            self.modifyform.num_list.append(self.staffmsg.item(i,0).text())
        self.modifyform.show()
        
    def search(self):
        tmp_list = ['工号','姓名','性别','岗位','基本工资','奖金','总工资']
        result = QStandardItemModel()
        for i in range(len(tmp_list)):
            result.setHorizontalHeaderItem(i,QStandardItem(tmp_list[i]))
            
        keyword = self.lineCondition.text()
        if self.boxCondition.currentText()=='工号':
            for i in self.stafflist:
                if keyword in i.getNum():
                    tmp = [QStandardItem(i.getNum()),QStandardItem(i.getName()),QStandardItem(i.getGender()),QStandardItem(i.getPost()),QStandardItem(str(i.getScore()['基本工资'])),QStandardItem(str(i.getScore()['奖金'])),QStandardItem(str(i.getTotal()))]
                    result.appendRow(tmp)
        elif self.boxCondition.currentText()=='姓名': 
            for i in self.stafflist:
                if keyword in i.getName():
                    tmp = [QStandardItem(i.getNum()),QStandardItem(i.getName()),QStandardItem(i.getGender()),QStandardItem(i.getPost()),QStandardItem(str(i.getScore()['基本工资'])),QStandardItem(str(i.getScore()['奖金'])),QStandardItem(str(i.getTotal()))]
                    result.appendRow(tmp)
        elif self.boxCondition.currentText()=='性别':
            for i in self.stafflist:
                if keyword in i.getGender():
                    tmp = [QStandardItem(i.getNum()),QStandardItem(i.getName()),QStandardItem(i.getGender()),QStandardItem(i.getPost()),QStandardItem(str(i.getScore()['基本工资'])),QStandardItem(str(i.getScore()['奖金'])),QStandardItem(str(i.getTotal()))]
                    result.appendRow(tmp)
        else:
            for i in self.stafflist:
                if keyword in i.getPost():
                    tmp = [QStandardItem(i.getNum()),QStandardItem(i.getName()),QStandardItem(i.getGender()),QStandardItem(i.getPost()),QStandardItem(str(i.getScore()['基本工资'])),QStandardItem(str(i.getScore()['奖金'])),QStandardItem(str(i.getTotal()))]
                    result.appendRow(tmp)
        
        result.sort(0,QtCore.Qt.AscendingOrder)
        self.tableSearch.setModel(result)           
    
    def createAction(self,num,name,gender,post,salary,bonus):
        total = float(salary)+float(bonus)
        total = str(total)
        tmp = [QStandardItem(num),QStandardItem(name),QStandardItem(gender),QStandardItem(post),QStandardItem(salary),QStandardItem(bonus),QStandardItem(total)]
        self.staffmsg.appendRow(tmp)
        if self.boxSort.currentText()=='工号':
            self.staffmsg.sort(0,QtCore.Qt.AscendingOrder)
        elif self.boxSort.currentText()=='姓名':
            self.staffmsg.sort(1,QtCore.Qt.AscendingOrder)
        else:
            self.staffmsg.sort(6,QtCore.Qt.DescendingOrder)
            
        self.averageSalary()
    
    def modifyAction(self,num,name,gender,post,salary,bonus):
        #获取当前选中的员工
        index = self.tableStaff.currentIndex().row()
        #计算总工资
        total = float(salary)+float(bonus)
        total = str(total)
        
        self.staffmsg.setItem(index,0,QStandardItem(num))
        self.staffmsg.setItem(index,1,QStandardItem(name))
        self.staffmsg.setItem(index,2,QStandardItem(gender))
        self.staffmsg.setItem(index,3,QStandardItem(post))
        self.staffmsg.setItem(index,4,QStandardItem(salary))
        self.staffmsg.setItem(index,5,QStandardItem(bonus))
        self.staffmsg.setItem(index,6,QStandardItem(total))
        
        if self.boxSort.currentText()=='工号':
            self.staffmsg.sort(0,QtCore.Qt.AscendingOrder)
        elif self.boxSort.currentText()=='姓名':
            self.staffmsg.sort(1,QtCore.Qt.AscendingOrder)
        else:
            self.staffmsg.sort(6,QtCore.Qt.DescendingOrder)
            
        self.averageSalary()   
    
    def highestSalary(self):
        tmp_list = ['工号','姓名','性别','岗位','基本工资','奖金','总工资']
        result = QStandardItemModel()
        for i in range(len(tmp_list)):
            result.setHorizontalHeaderItem(i,QStandardItem(tmp_list[i]))
        
        max_salary = 0
        max_bonus = 0
        index_salary = 0
        index_bonus = 0
        
        for i in range(self.staffmsg.rowCount()):
            if max_salary < float(self.staffmsg.item(i,4).text()):
                max_salary = float(self.staffmsg.item(i,4).text())
                index_salary = i
            if max_bonus < float(self.staffmsg.item(i,5).text()):
                max_bonus = float(self.staffmsg.item(i,5).text())
                index_bonus = i
        
        result.setItem(0,0,QStandardItem(self.staffmsg.item(index_salary,0).text()))
        result.setItem(0,1,QStandardItem(self.staffmsg.item(index_salary,1).text()))
        result.setItem(0,2,QStandardItem(self.staffmsg.item(index_salary,2).text()))
        result.setItem(0,3,QStandardItem(self.staffmsg.item(index_salary,3).text()))
        result.setItem(0,4,QStandardItem(self.staffmsg.item(index_salary,4).text()))
        result.setItem(0,5,QStandardItem(self.staffmsg.item(index_salary,5).text()))
        result.setItem(0,6,QStandardItem(self.staffmsg.item(index_salary,6).text()))
        
        result.setItem(1,0,QStandardItem(self.staffmsg.item(index_bonus,0).text()))
        result.setItem(1,1,QStandardItem(self.staffmsg.item(index_bonus,1).text()))
        result.setItem(1,2,QStandardItem(self.staffmsg.item(index_bonus,2).text()))
        result.setItem(1,3,QStandardItem(self.staffmsg.item(index_bonus,3).text()))
        result.setItem(1,4,QStandardItem(self.staffmsg.item(index_bonus,4).text()))
        result.setItem(1,5,QStandardItem(self.staffmsg.item(index_bonus,5).text()))
        result.setItem(1,6,QStandardItem(self.staffmsg.item(index_bonus,6).text()))
        
        
        self.tableSalary.setModel(result)
            
    def lowestSalary(self):
        tmp_list = ['工号','姓名','性别','岗位','基本工资','奖金','总工资']
        result = QStandardItemModel()
        for i in range(len(tmp_list)):
            result.setHorizontalHeaderItem(i,QStandardItem(tmp_list[i]))
            
        min_salary = float(self.staffmsg.item(0,4).text())
        min_bonus = float(self.staffmsg.item(0,5).text())
        index_salary = 0
        index_bonus = 0
        
        for i in range(self.staffmsg.rowCount()):
            if min_salary > float(self.staffmsg.item(i,4).text()):
                min_salary = float(self.staffmsg.item(i,4).text())
                index_salary = i
            if min_bonus > float(self.staffmsg.item(i,5).text()):
                min_bonus = float(self.staffmsg.item(i,5).text())
                index_bonus = i
        
        result.setItem(0,0,QStandardItem(self.staffmsg.item(index_salary,0).text()))
        result.setItem(0,1,QStandardItem(self.staffmsg.item(index_salary,1).text()))
        result.setItem(0,2,QStandardItem(self.staffmsg.item(index_salary,2).text()))
        result.setItem(0,3,QStandardItem(self.staffmsg.item(index_salary,3).text()))
        result.setItem(0,4,QStandardItem(self.staffmsg.item(index_salary,4).text()))
        result.setItem(0,5,QStandardItem(self.staffmsg.item(index_salary,5).text()))
        result.setItem(0,6,QStandardItem(self.staffmsg.item(index_salary,6).text()))
        
        result.setItem(1,0,QStandardItem(self.staffmsg.item(index_bonus,0).text()))
        result.setItem(1,1,QStandardItem(self.staffmsg.item(index_bonus,1).text()))
        result.setItem(1,2,QStandardItem(self.staffmsg.item(index_bonus,2).text()))
        result.setItem(1,3,QStandardItem(self.staffmsg.item(index_bonus,3).text()))
        result.setItem(1,4,QStandardItem(self.staffmsg.item(index_bonus,4).text()))
        result.setItem(1,5,QStandardItem(self.staffmsg.item(index_bonus,5).text()))
        result.setItem(1,6,QStandardItem(self.staffmsg.item(index_bonus,6).text()))
        
        self.tableSalary.setModel(result)
            
    def averageSalary(self):
        sum = 0
        for i in range(self.staffmsg.rowCount()):
            sum = sum + float(self.staffmsg.item(i,6).text())
        avg = sum/self.staffmsg.rowCount()
        avg = str(avg)
        self.lineAvg.setText(avg)
        
    def sortSalary(self):
        if self.boxSalary.currentText()=='各类工资最高':
            self.highestSalary()
        else:
            self.lowestSalary()
