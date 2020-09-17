# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\java\c4挑战赛\form_3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from data.int_brief import Brief

class Ui_form_3(object):
#     def init(self):
#         self.spanning=SpanningTree()
#         self.spanning_response=self.spanning.get_SpanningTree_response()
        
    def setupUi(self, form_3):
        form_3.setObjectName("form_3")
        form_3.resize(788, 380)
        form_3.setStyleSheet("background-color: qconicalgradient(cx:0.482955, cy:0, angle:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        

        
        self.textBrowser_3 = QtWidgets.QTextBrowser(form_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(40, 40, 711, 301))
        self.textBrowser_3.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(form_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 60, 711, 241))
        self.tableWidget_2.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        
        
        
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(78, 173, 255))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.pushButton_3 = QtWidgets.QPushButton(form_3)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 310, 91, 21))
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(form_3)
        self.label_7.setGeometry(QtCore.QRect(50, 310, 61, 20))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(form_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 310, 191, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(form_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 310, 151, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_6 = QtWidgets.QLabel(form_3)
        self.label_6.setGeometry(QtCore.QRect(250, 310, 201, 20))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(form_3)
        QtCore.QMetaObject.connectSlotsByName(form_3)

    def retranslateUi(self, form_3):
#         self.spanning_response=self.spanning.get_SpanningTree_response()
        _translate = QtCore.QCoreApplication.translate
        form_3.setWindowTitle(_translate("form_3", "交换机接口配置信息"))
        self.textBrowser_3.setHtml(_translate("form_3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">交换机接口配置信息</span></p></body></html>"))

        
        
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("form_3", "interface"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("form_3", "ip_addr"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("form_3", "speed"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("form_3", "state"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("form_3", "portmode"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("form_3", "type"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("form_3", "vlan"))
        
        self.brief=Brief()
        self.brief_response=self.brief.get_brief_response()
#         device['interface'],
#                   device['speed'],
#                   device['state'],
#                   device['portmode'],
#                   device['type'],
#                   device['vlan']
#         self.spanning_response=self.spanning.get_SpanningTree_response()



        rowPostion=self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(rowPostion)
        self.tableWidget_2.setItem(rowPostion,0,QTableWidgetItem(self.brief_response['ROW_interface'][0]['interface']))
        self.tableWidget_2.setItem(rowPostion,1,QTableWidgetItem(self.brief_response['ROW_interface'][0]['ip_addr']))
        self.tableWidget_2.setItem(rowPostion,2,QTableWidgetItem(self.brief_response['ROW_interface'][0]['speed']))
        self.tableWidget_2.setItem(rowPostion,3,QTableWidgetItem(self.brief_response['ROW_interface'][0]['state']))
        count=0
        for device in self.brief_response['ROW_interface']:
            rowPostion=self.tableWidget_2.rowCount()
            if(count!=0):
                self.tableWidget_2.insertRow(rowPostion)
                self.tableWidget_2.setItem(rowPostion,0,QTableWidgetItem(device['interface']))
                self.tableWidget_2.setItem(rowPostion,2,QTableWidgetItem(device['speed']))
                self.tableWidget_2.setItem(rowPostion,3,QTableWidgetItem(device['state']))
                self.tableWidget_2.setItem(rowPostion,4,QTableWidgetItem(device['portmode']))
                self.tableWidget_2.setItem(rowPostion,5,QTableWidgetItem(device['type']))
                self.tableWidget_2.setItem(rowPostion,6,QTableWidgetItem(device['vlan']))
            count+=1
                
            
#             self.tableWidget_2.setItem(rowPostion,6,QTableWidgetItem(device['oper_p2p']))
                
#             print("{0:20}{1:15}{2:15}{3:10}{4:14}{5:12}{6:10}".
#             format(device['if_index'],
#                   device['role'],
#                    device['state'],
#                   device['path_cost'],
#                   device['port_priority'],
#                   device['port_number'],
#                   device['oper_p2p']))
#          
#         rowPostion=self.tableWidget_2.rowCount()
#         self.tableWidget_2.insertRow(rowPostion)
#         self.tableWidget_2.setItem(rowPostion,0,QTableWidgetItem("regf"))
        
        
        self.pushButton_3.setText(_translate("form_3", "查  看"))
        self.label_7.setText(_translate("form_3", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">vlan：</span></p></body></html>"))
        self.label_6.setText(_translate("form_3", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">查看MAC address的状态：</span></p></body></html>"))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_form_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
