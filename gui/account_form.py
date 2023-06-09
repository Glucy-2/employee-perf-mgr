# -*- coding: utf-8 -*-

from PySide6.QtWidgets import *
import account
from gui import ui_account
from gui import msgbox
from gui import manage_form


class Window(QMainWindow, ui_account.Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # 要操作的控件
        # self.username_line = self.ui.username_line  # 用户名输入框
        # self.password_line = self.ui.password_line  # 密码输入框
        # self.login_btn = self.ui.login_btn  # 登录按钮
        # self.change_password_btn = self.ui.change_password_btn  # 修改密码按钮
        # self.manage_btn = self.ui.manage_btn  # 管理按钮

        if account.logged_in:  # 如果已经登录
            self.login_btn.setEnabled(False)  # 设置登录按钮不可用
            self.change_password_btn.setEnabled(True)  # 设置修改密码按钮可用
            self.manage_btn.setEnabled(True)  # 设置管理按钮可用
        else:  # 如果没有登录
            self.login_btn.setEnabled(True)
            self.change_password_btn.setEnabled(False)
            self.manage_btn.setEnabled(False)

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login)  # 按了登陆按钮后开始login函数
        self.change_password_btn.clicked.connect(
            self.change_pwd
        )  # 按了修改密码按钮后开始change_pwd函数
        self.manage_btn.clicked.connect(self.manage)  # 按了显示框按钮后开始manage函数
        self.username_line.returnPressed.connect(
            self.return_pressed
        )  # 用户名输入框中按了回车键后就开始return_pressed函数
        self.password_line.returnPressed.connect(
            self.return_pressed
        )  # 密码输入框中按了回车键后就开始return_pressed函数

    def return_pressed(self):
        if self.login_btn.isEnabled():
            self.login()
        elif self.change_password_btn.isEnabled():
            self.change_pwd()

    def login(self):
        if not account.logged_in:  # 如果没有登录
            username = self.username_line.text()  # 获取用户名
            if username == "admin":  # 如果用户名正确
                password = self.password_line.text()  # 获取密码
                result = account.check(account.encrypt(password))  # 登录
                if result[0]:  # 如果检查失败
                    msgbox.error("登录失败", f"错误信息：{result}")  # 显示错误对话框
                elif result[1]:  # 如果检查成功并且密码正确
                    account.logged_in = True  # 设置已登录
                    self.login_btn.setEnabled(False)  # 设置登录按钮不可用
                    self.change_password_btn.setEnabled(True)  # 设置修改密码按钮可用
                    self.manage_btn.setEnabled(True)  # 设置管理按钮可用
                    msgbox.info("登录成功", "欢迎使用本系统")  # 显示提示对话框
                else:  # 如果检查成功但密码错误
                    msgbox.error("登录失败", "密码错误")  # 显示错误对话框
                    return
            else:
                msgbox.error("登录失败", "用户名错误")  # 显示错误对话框
        else:  # 如果已经登录
            msgbox.info("已登录", "您已经登录了")  # 显示提示对话框

    def change_pwd(self):
        if account.logged_in:  # 如果已经登录
            username = self.username_line.text()  # 获取用户名
            if username == "admin":  # 如果用户名正确
                password = self.password_line.text()  # 获取密码
                result = account.write(account.encrypt(password))  # 修改密码
                if result:  # 如果修改失败
                    msgbox.error("修改密码失败", f"错误信息：{result}")  # 显示错误对话框
                else:  # 如果修改成功
                    msgbox.info("修改密码成功", "请重新登录")  # 显示提示对话框
                    account.logged_in = False  # 设置未登录
                    self.login_btn.setEnabled(True)  # 设置登录按钮可用
                    self.change_password_btn.setEnabled(False)  # 设置修改密码按钮不可用
                    self.manage_btn.setEnabled(False)  # 设置管理按钮不可用
            else:
                msgbox.error("修改密码失败", "用户名错误")
        else:  # 如果没有登录
            msgbox.error("修改密码失败", "请先登录")  # 显示错误对话框

    def manage(self):
        if account.logged_in:
            self.hide()  # 隐藏自身窗口
            try:
                w = manage_form.Window()  # 设置管理窗口
                w.exec_()
                self.show()  # 显示自身窗口
            except Exception as e:
                msgbox.error("打开管理窗口时发生错误", f"错误信息：{e}")
        else:
            msgbox.error("打开管理窗口失败", "请先登录")


def show():
    app = QApplication.instance() or QApplication([])  # 获取或创建 QApplication 对象
    try:
        w = Window()
        # 展示窗口
        w.show()
        app.exec()
    except Exception as e:
        msgbox.error("打开账户窗口时发生错误", f"错误信息：{e}")
    finally:
        # 在应用程序关闭之前停止Qt对象的运行
        app.quit()
