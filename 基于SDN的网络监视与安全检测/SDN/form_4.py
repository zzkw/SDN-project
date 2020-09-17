# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\java\c4挑战赛\form_4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from data.spanning_tree import SpanningTree

class Ui_form_4:
    
    def setupUi(self, form_4):
        form_4.setObjectName("form_4")
        form_4.resize(774, 369)
        form_4.setStyleSheet("background-color: qconicalgradient(cx:0.482955, cy:0, angle:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget = QtWidgets.QTableWidget(form_4)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 711, 241))
        self.tableWidget.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(78, 173, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton = QtWidgets.QPushButton(form_4)
        self.pushButton.setGeometry(QtCore.QRect(350, 300, 91, 21))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(form_4)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 711, 301))
        self.textBrowser.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.raise_()
        self.tableWidget.raise_()
        self.pushButton.raise_()

        self.retranslateUi(form_4)
        QtCore.QMetaObject.connectSlotsByName(form_4)

    def retranslateUi(self, form_4):
        _translate = QtCore.QCoreApplication.translate
        form_4.setWindowTitle(_translate("form_4", "交换机接口链路信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("form_4", "interface"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("form_4", "role"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("form_4", "start"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("form_4", "path_cost"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("form_4", "port_priority"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("form_4", "port_number"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("form_4", "oper_p2p"))
        
        
        self.spanning=SpanningTree()
        self.spanning_response=self.spanning.get_SpanningTree_response()
        
        for device in self.spanning_response['ROW_port']:
            rowPostion=self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPostion)
            self.tableWidget.setItem(rowPostion,0,QTableWidgetItem(device['if_index']))
            self.tableWidget.setItem(rowPostion,1,QTableWidgetItem(device['role']))
            self.tableWidget.setItem(rowPostion,2,QTableWidgetItem(device['state']))
            self.tableWidget.setItem(rowPostion,3,QTableWidgetItem(device['path_cost']))
            self.tableWidget.setItem(rowPostion,4,QTableWidgetItem(device['port_priority']))
            self.tableWidget.setItem(rowPostion,5,QTableWidgetItem(device['port_number']))
            self.tableWidget.setItem(rowPostion,6,QTableWidgetItem(device['oper_p2p']))
        
        
        self.pushButton.setText(_translate("form_4", "刷   新"))
        self.textBrowser.setHtml(_translate("form_4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">交换机接口链路信息</span></p></body></html>"))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_form_4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
