from Ui_Create import Ui_InputForm
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QCoreApplication, Qt
import re


class CreateForm(QWidget,Ui_InputForm):
    confirm_create_signal = pyqtSignal(str,str,str,str,str,str)
    num_list = []
    
    def __init__(self,*args,**kwargs):
        super(CreateForm,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.btnCreate.setText('添加')
        
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        
        self.btnCreate.clicked.connect(self.create)
        
    def create(self):
        num = self.lineNum.text()
        name = self.lineName.text()
        gender = self.boxGender.currentText()
        post = self.boxPost.currentText()
        salary = self.lineSalary.text()
        bonus = self.lineBonus.text()
        
        #用正则表达式判断非法输入
        #设置工号的格式为B+数字
        rules = re.compile('^B\d+$')
        if not rules.findall(num):
            QMessageBox.warning(self,"非法输入","工号的格式必须为B+数字，如B01")
            return
            
        #名字中不允许出现数字
        rules = re.compile('\d+')
        if rules.findall(name):
            QMessageBox.warning(self,"非法输入","名字中不能含有数字")
            return
        
        #工资类数据必须为固定格式的金额
        rules = re.compile('^\d+\.\d+$')
        if not rules.findall(salary):
            QMessageBox.warning(self,"非法输入","基本工资必须为一个金额，且精确到小数点后1位，如2000.0")
            return
        if not rules.findall(bonus):
            QMessageBox.warning(self,"非法输入","奖金必须为一个金额，且精确到小数点后1位，如2000.0")
            return
        
        if num in self.num_list:
            QMessageBox.warning(self,"警告","工号已存在")
            return

        reply = QMessageBox.question(self,'提示','是否确认创建？',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            self.confirm_create_signal.emit(num,name,gender,post,salary,bonus)
            QMessageBox.information(self,'提示','创建成功！')
            self.close()
        else:
            return
