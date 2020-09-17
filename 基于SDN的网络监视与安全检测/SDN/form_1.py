# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\java\c4挑战赛\form_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from data.version1 import Item
from data.get_sys_time import SysInfo


import time
import threading
 


class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter, ui):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.ui=ui
    def run(self):
        while 1:                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
            self.ui.auto_refresh()
        
        
class Ui_form_1(object):
    def __init__(self):
        self.vv=Item()
        self.response=self.vv.print_version()
        self.ss=SysInfo()
        self.sysInfo=self.ss.running_time()
        self.running_time=self.sysInfo["systemUpTime"]
        
    def setupUi(self, form_1):
        
        msg=self.response["msg"]
        chassis_id=self.response["body"]["chassis_id"]
        version=self.response["body"]["kickstart_ver_str"]
        form_1.setObjectName("form_1")
        form_1.resize(692, 236)
        form_1.setStyleSheet("background-color: qconicalgradient(cx:0.482955, cy:0, angle:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit_3 = QtWidgets.QLineEdit(form_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(426, 100, 151, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText(version)
        self.lineEdit_3.setReadOnly(True)
        self.label_5 = QtWidgets.QLabel(form_1)
        self.label_5.setGeometry(QtCore.QRect(46, 140, 91, 16))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(form_1)
        self.label_4.setGeometry(QtCore.QRect(326, 100, 91, 16))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(form_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(426, 60, 151, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText(msg)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_4 = QtWidgets.QLineEdit(form_1)
        self.lineEdit_4.setGeometry(QtCore.QRect(146, 100, 151, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText(chassis_id)
        self.lineEdit_4.setReadOnly(True)
        self.label_3 = QtWidgets.QLabel(form_1)
        self.label_3.setGeometry(QtCore.QRect(46, 100, 91, 16))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(form_1)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 170, 111, 23))
        self.pushButton_2.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        self.pushButton_2.clicked.connect(self.refresh)


        self.lineEdit_5 = QtWidgets.QLineEdit(form_1)
        self.lineEdit_5.setGeometry(QtCore.QRect(146, 140, 431, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText(self.running_time)
        self.lineEdit_5.setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(form_1)
        self.label_2.setGeometry(QtCore.QRect(326, 60, 91, 16))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(form_1)
        self.lineEdit.setGeometry(QtCore.QRect(146, 60, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        hostname=self.response["body"]["host_name"]
        self.lineEdit.setPlaceholderText(hostname)
       
        self.label = QtWidgets.QLabel(form_1)
        self.label.setGeometry(QtCore.QRect(46, 60, 91, 16))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(form_1)
        self.textEdit_2.setGeometry(QtCore.QRect(36, 30, 641, 181))
        self.textEdit_2.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_4.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_5.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label.raise_()

        self.retranslateUi(form_1)
        QtCore.QMetaObject.connectSlotsByName(form_1)

    def retranslateUi(self, form_1):
        _translate = QtCore.QCoreApplication.translate
        form_1.setWindowTitle(_translate("form_1", "交换机基本信息"))
        self.label_5.setText(_translate("form_1", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">uptime</span></p></body></html>"))
        self.label_4.setText(_translate("form_1", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">version</span></p></body></html>"))
        self.label_3.setText(_translate("form_1", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">chassis_id</span></p></body></html>"))
        self.pushButton_2.setText(_translate("form_1", "刷新"))
        self.label_2.setText(_translate("form_1", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">msg</span></p></body></html>"))
        self.label.setText(_translate("form_1", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">hostname</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("form_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">交换机信息</span></p></body></html>"))
    
    def refresh(self):
        self.response=self.vv.print_version()
        hostname=self.response["body"]["host_name"]
        self.lineEdit.setPlaceholderText(hostname)
        
        
    def auto_refresh(self):
        self.sysInfo=self.ss.running_time()
        self.running_time=self.sysInfo["systemUpTime"]
        self.lineEdit_5.setPlaceholderText(self.running_time)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_form_1()
    ui.setupUi(MainWindow)
    
    thread1 = myThread(1, "Thread-1", 1, ui)
    thread1.start()
    
    MainWindow.show()
    sys.exit(app.exec_())
