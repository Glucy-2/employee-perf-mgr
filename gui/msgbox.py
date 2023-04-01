# -*- coding: utf-8 -*-

# 弹窗模块，用于显示错误/警告/信息并返回结果
# 传入信息，详细信息和是否要显示取消按钮，返回是否点击了确认按钮

from PySide6.QtWidgets import QApplication, QMessageBox


def error(msg, info, show_cancel_btn=False):  # 显示错误对话框
    app = QApplication.instance() or QApplication([])  # 获取或创建 QApplication 对象
    msg_box = QMessageBox()  # 创建错误对话框
    msg_box.setIcon(QMessageBox.Critical)  # 设置图标为错误
    msg_box.setText(msg)  # 设置错误信息
    msg_box.setInformativeText(info)  # 设置详细信息
    msg_box.setWindowTitle("错误")  # 设置标题
    if show_cancel_btn:  # 如果要显示取消按钮
        btns = QMessageBox.Ok | QMessageBox.Cancel
    else:  # 如果不要显示取消按钮
        btns = QMessageBox.Ok
    msg_box.setStandardButtons(btns)  # 设置按钮，确认和取消
    msg_box.setDefaultButton(QMessageBox.Ok)  # 设置默认按钮
    return_value = msg_box.exec_()  # 显示对话框并获取返回值
    if return_value == QMessageBox.Ok:  # 如果点击了确认按钮
        msg_box.close()
        return True
    else:  # 如果点击了取消按钮
        msg_box.close()
        return False


def warning(msg, info, show_cancel_btn=False):  # 显示警告对话框
    app = QApplication.instance() or QApplication([])  # 获取或创建 QApplication 对象
    msg_box = QMessageBox()  # 创建警告对话框
    msg_box.setIcon(QMessageBox.Warning)  # 设置图标为警告
    msg_box.setText(msg)  # 设置警告信息
    msg_box.setInformativeText(info)  # 设置详细信息
    msg_box.setWindowTitle("警告")  # 设置标题
    if show_cancel_btn:  # 如果要显示取消按钮
        btns = QMessageBox.Ok | QMessageBox.Cancel
    else:  # 如果不要显示取消按钮
        btns = QMessageBox.Ok
    msg_box.setStandardButtons(btns)  # 设置按钮，确认和取消
    msg_box.setDefaultButton(QMessageBox.Ok)  # 设置默认按钮
    return_value = msg_box.exec_()  # 显示对话框并获取返回值
    if return_value == QMessageBox.Ok:  # 如果点击了确认按钮
        msg_box.close()
        return True
    else:  # 如果点击了取消按钮
        msg_box.close()
        return False


def info(msg, info, show_cancel_btn=False):  # 显示信息对话框
    app = QApplication.instance() or QApplication([])  # 获取或创建 QApplication 对象
    msg_box = QMessageBox()  # 创建信息对话框
    msg_box.setIcon(QMessageBox.Information)  # 设置图标为信息
    msg_box.setText(msg)  # 设置信息
    msg_box.setInformativeText(info)  # 设置详细信息
    msg_box.setWindowTitle("信息")  # 设置标题
    if show_cancel_btn:  # 如果要显示取消按钮
        btns = QMessageBox.Ok | QMessageBox.Cancel
    else:  # 如果不要显示取消按钮
        btns = QMessageBox.Ok
    msg_box.setStandardButtons(btns)  # 设置按钮，确认和取消
    msg_box.setDefaultButton(QMessageBox.Ok)  # 设置默认按钮
    return_value = msg_box.exec_()  # 显示对话框并获取返回值
    if return_value == QMessageBox.Ok:  # 如果点击了确认按钮
        msg_box.close()
        return True
    else:  # 如果点击了取消按钮
        msg_box.close()
        return False
