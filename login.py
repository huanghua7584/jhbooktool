# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        Form.setMinimumSize(QtCore.QSize(500, 300))
        Form.setMaximumSize(QtCore.QSize(500, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/bluebooklogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.logoimage = QtWidgets.QLabel(Form)
        self.logoimage.setGeometry(QtCore.QRect(80, 10, 120, 130))
        self.logoimage.setStyleSheet("")
        self.logoimage.setText("")
        self.logoimage.setPixmap(QtGui.QPixmap("images/titlelogo.png"))
        self.logoimage.setScaledContents(True)
        self.logoimage.setObjectName("logoimage")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(200, 30, 220, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.edit_name = QtWidgets.QLineEdit(Form)
        self.edit_name.setGeometry(QtCore.QRect(193, 150, 113, 21))
        self.edit_name.setObjectName("edit_name")
        self.edit_password = QtWidgets.QLineEdit(Form)
        self.edit_password.setGeometry(QtCore.QRect(193, 190, 113, 21))
        self.edit_password.setObjectName("edit_password")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(193, 220, 113, 24))
        self.btn_login.setObjectName("btn_login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.title.setText(_translate("Form", "建河图书工具系统"))
        self.edit_name.setPlaceholderText(_translate("Form", "用户名"))
        self.edit_password.setPlaceholderText(_translate("Form", "密码"))
        self.btn_login.setText(_translate("Form", "登录"))