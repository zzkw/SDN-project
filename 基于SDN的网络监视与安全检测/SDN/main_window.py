# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\java\c4挑战赛\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 445)
        MainWindow.setStyleSheet("background-image: url(../img/88.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 130,112, 41))
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(102, 204, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 110,112, 41))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(102, 204, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 220, 112, 41))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(102, 204, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 340, 112, 41))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(102, 204, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 260, 112, 41))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(102, 204, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionfrom_1 = QtWidgets.QAction(MainWindow)
        self.actionfrom_1.setObjectName("actionfrom_1")
        self.actionfrom_2 = QtWidgets.QAction(MainWindow)
        self.actionfrom_2.setObjectName("actionfrom_2")
        self.actionfrom_3 = QtWidgets.QAction(MainWindow)
        self.actionfrom_3.setObjectName("actionfrom_3")
        self.actionfrom_4 = QtWidgets.QAction(MainWindow)
        self.actionfrom_4.setObjectName("actionfrom_4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于SDN的网络监视和安全检测"))
        self.pushButton.setText(_translate("MainWindow", "交换机基本信息"))
        self.pushButton_2.setText(_translate("MainWindow", "交换机接口链路信息"))
        self.pushButton_3.setText(_translate("MainWindow", "交换机接口配置信息"))
        self.pushButton_4.setText(_translate("MainWindow", "网络监视和安全检测"))
        self.pushButton_5.setText(_translate("MainWindow", "登   录"))
        self.actionfrom_1.setText(_translate("MainWindow", "from_1"))
        self.actionfrom_2.setText(_translate("MainWindow", "from_2"))
        self.actionfrom_3.setText(_translate("MainWindow", "from_3"))
        self.actionfrom_4.setText(_translate("MainWindow", "from_4"))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
