from Ui_Reg import Ui_RegForm
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, QCoreApplication

class RegForm(QWidget,Ui_RegForm):
    #reg_signal = pyqtSignal(str,str)
    account_dic = {}
    
    def __init__(self,*args,**kwargs):
        super(RegForm,self).__init__(*args,**kwargs)
        self.setupUi(self)
        
        self.btnReg.clicked.connect(self.reg)

    def reg(self):
        if self.lineAccount.text().strip()=='' or self.linePwd.text().strip()=='':
            QMessageBox.warning(self,'错误','账号和密码均不能为空')
            return
        #self.reg_signal.emit(self.lineAccount.text(),self.linePwd.text())
        if self.lineAccount.text() in self.account_dic.keys():
            QMessageBox.warning(self,'错误','该用户名已经被占用')
            return
        else:
            self.account_dic[self.lineAccount.text()]=self.linePwd.text()
            QMessageBox.information(self,'提示','注册成功')
        self.close()
