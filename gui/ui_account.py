# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(767, 335)
        Form.setMaximumSize(QSize(1444, 898))
        self.username_line = QLineEdit(Form)
        self.username_line.setObjectName(u"username_line")
        self.username_line.setGeometry(QRect(160, 40, 581, 51))
        font = QFont()
        font.setPointSize(20)
        self.username_line.setFont(font)
        self.username_line.setTabletTracking(False)
        self.password_line = QLineEdit(Form)
        self.password_line.setObjectName(u"password_line")
        self.password_line.setGeometry(QRect(160, 140, 581, 51))
        self.password_line.setFont(font)
        self.password_line.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(30, 220, 271, 71))
        self.login_btn.setFont(font)
        self.username_label = QLabel(Form)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(30, 30, 111, 71))
        self.username_label.setFont(font)
        self.password_label = QLabel(Form)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(30, 120, 111, 81))
        self.password_label.setFont(font)
        self.change_password_btn = QPushButton(Form)
        self.change_password_btn.setObjectName(u"change_password_btn")
        self.change_password_btn.setGeometry(QRect(320, 220, 201, 71))
        self.change_password_btn.setFont(font)
        self.manage_btn = QPushButton(Form)
        self.manage_btn.setObjectName(u"manage_btn")
        self.manage_btn.setGeometry(QRect(540, 220, 201, 71))
        self.manage_btn.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6b22\u8fce\u60a8\u4f7f\u7528\u4f01\u4e1a\u5458\u5de5\u4e1a\u7ee9\u7ba1\u7406\u7cfb\u7edf", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.username_label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.password_label.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.change_password_btn.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u5bc6\u7801", None))
        self.manage_btn.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406", None))
    # retranslateUi

