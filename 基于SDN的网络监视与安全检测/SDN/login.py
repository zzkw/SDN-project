# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\java\c4挑战赛\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from data.version1 import Item
from SDN.switch_login_info import SwitchLoginInfo

from SDN.main_window import *
from SDN.form_1 import *
from SDN.form_2 import *
from SDN.form_3 import *
from SDN.form_4 import *
from PyQt5.QtWidgets import QLineEdit

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(496, 274)
        Form.setStyleSheet("background-color: qconicalgradient(cx:0.482955, cy:0, angle:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 140, 151, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 90, 91, 16))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 40, 91, 16))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 90, 151, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 140, 91, 16))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 40, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">用户名</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">IP地址</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">密   码</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "登  录"))
      
        self.pushButton_2.setText(_translate("Form", "取  消"))
    
        
    def login(self):
        ip_address=self.lineEdit.text()
        username=self.lineEdit_4.text()
        password=self.lineEdit_3.text()
        vv=Item(ip_address,username,password)
        response=vv.print_version()
        if(response["code"]=="200"):
            switch=SwitchLoginInfo()
            switch.changeUserInfo(ip_address, username, password)

            self.ifSucess=True
        else:
            self.ifSucess=False
    def cancel(self):
        a=0

           
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    login_1= QtWidgets.QDialog()      
    login_ui = Ui_Form()
    login_ui.setupUi(login_1)
    
    MainWindow = QtWidgets.QMainWindow()
    main_ui = Ui_MainWindow()
    main_ui.setupUi(MainWindow)
    
    
    brn=login_ui.pushButton
    brn.clicked.connect(MainWindow.show)
    brn.clicked.connect(login_1.close)
    
     # 实例化子窗口 
    child_1 = QtWidgets.QDialog()
    child_ui = Ui_form_1()
    child_ui.setupUi(child_1)
    thread1 = myThread(1, "Thread-1", 1, child_ui)
    thread1.start()
      
    child_2 = QtWidgets.QDialog()      
    child_ui = Ui_form_2()
    child_ui.setupUi(child_2)
      
    child_3 = QtWidgets.QDialog()      
    child_ui = Ui_form_3()
    child_ui.setupUi(child_3)
      
    child_4 = QtWidgets.QDialog()      
    child_ui = Ui_form_4()
    child_ui.setupUi(child_4)
      
    child_5 = QtWidgets.QDialog()      
    child_ui = Ui_Form()
    child_ui.setupUi(child_5)
       
      # 按钮绑定事件
    btn_1 = main_ui.pushButton
    btn_1.clicked.connect(child_1.show)
      
    btn_2 = main_ui.pushButton_2
    btn_2.clicked.connect(child_4.show) 
      
    btn_3 = main_ui.pushButton_3
    btn_3.clicked.connect(child_3.show) 
      
    btn_4 = main_ui.pushButton_4
    btn_4.clicked.connect(child_2.show)
      
    btn_5 = main_ui.pushButton_5
    btn_5.clicked.connect(child_5.show)
    
    
    login_1.show()
    sys.exit(app.exec_())
    
        
        
    
    
    
