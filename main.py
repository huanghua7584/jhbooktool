import sys
import pickle
import pandas as pd
import numpy as np
from login import *
from mainwindow import *
from Shared import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog, QTableView, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class login(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        self.setupUi(self)
        self.btn_login.clicked.connect(self.onLogin)
        self.edit_password.returnPressed.connect(self.onLogin)

    def onLogin(self):
        username = self.edit_name.text().strip()
        password = self.edit_password.text().strip()
        file = open("/Volumes/资料/gitfiles/jhbooktool/data/user.data", "rb")
        df = pickle.load(file)
        nameBool = username in df.name.values
        passBool = password in df.password.values
        file.close()
        if not nameBool or not passBool:
            QMessageBox.warning(self, "登录失败", "用户名或密码错误！")
            return
        SI.mainWin = winMain()
        #SI.mainWin.showMaximized() #窗口最大化
        SI.mainWin.show()
        self.hide()


class winMain(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(winMain, self).__init__(parent)
        self.setupUi(self)
        self.root.clicked.connect(self.dataTree)

    def dataTree(self, index):
        print(index.row())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SI.loginWin = login()
    SI.loginWin.show()
    sys.exit(app.exec_())
