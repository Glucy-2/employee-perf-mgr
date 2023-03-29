from Ui_Login import Ui_LoginForm
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, QCoreApplication, Qt
from ref.MainForm import MainForm
from RegForm import RegForm
import sys

class LoginForm(QWidget,Ui_LoginForm):
    close_signal = pyqtSignal()
    
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.setupUi(self)
        
        self.regform = RegForm()
        
        self.btnLogin.clicked.connect(self.Login)
        self.btnReg.clicked.connect(self.Reg)
        
    def Login(self):
        tmp = self.linePassword.text()
        if tmp=='':
            QMessageBox.warning(self, '错误', '密码为空')
        
        for i,j in self.regform.account_dic.items():
            if self.lineAccount.text() == i:
                if self.linePassword.text() == j:
                    self.close()
                    self.close_signal.emit()
                    return
        QMessageBox.warning(self, '错误', '用户名或密码错误')
            
    def Reg(self):
        self.regform.show()       
        
if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    w=LoginForm()
    w1=MainForm()

    w.show()
    w.close_signal.connect(w1.show_win)  #第一个窗体的信号连接第二个窗体的show_w1方法
    
    app.exec_()
