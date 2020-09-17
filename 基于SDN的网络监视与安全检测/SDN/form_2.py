# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\java\c4挑战赛\form_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from data.redundancy import Redundancy
from data.ip_route import IpRoute
from data.proc_log import ProcLog
import tkinter
from data.sys_reso import SysReso

class Ui_form_2(object):
    def __init__(self):
        self.red=Redundancy()
        self.redundancy_response=self.red.get_redundancy_response()
        self.ip_route=IpRoute()
        self.ip_route_response=self.ip_route.get_ip_response()
        self.procLog=ProcLog()
        self.proc_log_response=self.procLog.get_ProLog_response()
        self.sysReso=SysReso()
        self.sysReso_response=self.sysReso.get_SysReso_response()
    
    def setupUi(self, form_2):
        form_2.setObjectName("form_2")
        form_2.resize(670, 534)
        form_2.setStyleSheet("background-color: qconicalgradient(cx:0.482955, cy:0, angle:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_11 = QtWidgets.QLabel(form_2)
        self.label_11.setGeometry(QtCore.QRect(60, 330, 91, 21))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setObjectName("label_11")
        self.label_8 = QtWidgets.QLabel(form_2)
        self.label_8.setGeometry(QtCore.QRect(60, 50, 91, 121))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setObjectName("label_8")
        self.pushButton_6 = QtWidgets.QPushButton(form_2)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 240, 111, 23))
        self.pushButton_6.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget_4 = QtWidgets.QListWidget(form_2)
        self.listWidget_4.setGeometry(QtCore.QRect(160, 370, 291, 121))
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        
        self.pushButton_7 = QtWidgets.QPushButton(form_2)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 330, 111, 23))
        self.pushButton_7.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(form_2)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 420, 111, 23))
        self.pushButton_8.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_8.setObjectName("pushButton_8")
        self.listWidget_2 = QtWidgets.QListWidget(form_2)
        self.listWidget_2.setGeometry(QtCore.QRect(160, 190, 291, 121))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.listWidget_3 = QtWidgets.QListWidget(form_2)
        self.listWidget_3.setGeometry(QtCore.QRect(160, 330, 291, 21))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.pushButton_5 = QtWidgets.QPushButton(form_2)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 100, 111, 23))
        self.pushButton_5.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_5.setObjectName("pushButton_5")
        self.scrollArea = QtWidgets.QScrollArea(form_2)
        self.scrollArea.setGeometry(QtCore.QRect(40, 20, 591, 501))
        self.scrollArea.setStyleSheet("background-color: qconicalgradient(cx:0.477273, cy:0, angle:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 589, 499))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.label_9 = QtWidgets.QLabel(form_2)
        self.label_9.setGeometry(QtCore.QRect(60, 190, 91, 121))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setObjectName("label_9")
        self.listWidget = QtWidgets.QListWidget(form_2)
        self.listWidget.setGeometry(QtCore.QRect(160, 50, 291, 121))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_10 = QtWidgets.QLabel(form_2)
        self.label_10.setGeometry(QtCore.QRect(60, 370, 91, 121))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setObjectName("label_10")
        self.scrollArea.raise_()
        self.label_11.raise_()
        self.label_8.raise_()
        self.pushButton_6.raise_()
        self.listWidget_4.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.listWidget_2.raise_()
        self.listWidget_3.raise_()
        self.pushButton_5.raise_()
        self.label_9.raise_()
        self.listWidget.raise_()
        self.label_10.raise_()

        self.retranslateUi(form_2)
        QtCore.QMetaObject.connectSlotsByName(form_2)

    def retranslateUi(self, form_2):
        self.redundancy_response=self.red.get_redundancy_response()
        self.ip_route_response=self.ip_route.get_ip_response()
        self.proc_log_response=self.procLog.get_ProLog_response()
        self.sysReso_response=self.sysReso.get_SysReso_response()
        
        
        _translate = QtCore.QCoreApplication.translate
        form_2.setWindowTitle(_translate("form_2", "网络监视与安全检测"))
        self.label_11.setText(_translate("form_2", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">进程日志</span></p></body></html>"))
        self.label_8.setText(_translate("form_2", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">交换机的</span></p><p align=\"center\"><span style=\" font-size:10pt;\">冗余状态</span></p></body></html>"))
        self.pushButton_6.setText(_translate("form_2", "查   看"))
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        
        
#         self.sysReso_response=self.sysReso.get_SysReso_response()
#         print()
#         print()
#         print("CPU states  :   ",response['cpu_state_user'],"% user  ",response['cpu_state_kernel'],"% kernel  ",response['cpu_state_idle'],"% idle")
#         print("Memory usage:   ",response['memory_usage_total'],"K total  ",response['memory_usage_used'],"K used  ",response['memory_usage_free'],"K free")
#         print("Current memory status: ",response['current_memory_status'])
        item = self.listWidget_4.item(0)
        item.setText(_translate("form_2", "Load average:   "+"1 minute:"+str(self.sysReso_response['load_avg_1min'])+"  5 minutes:"+str(self.sysReso_response['load_avg_5min'])+"  15 minutes:"+str(self.sysReso_response['load_avg_15min'])))
        item = self.listWidget_4.item(1)
        item.setText(_translate("form_2", "Processes   :   "+str(self.sysReso_response['processes_total'])+"total  "+str(self.sysReso_response['processes_running'])+"running"))
        item = self.listWidget_4.item(2)
        item.setText(_translate("form_2", "CPU states  :   "+str(self.sysReso_response['cpu_state_user'])+"% user  "+str(self.sysReso_response['cpu_state_kernel'])+"% kernel  "+str(self.sysReso_response['cpu_state_idle'])+"% idle"))
        item = self.listWidget_4.item(3)
        item.setText(_translate("form_2", "Memory usage:   "+str(self.sysReso_response['memory_usage_total'])+"K total  "+str(self.sysReso_response['memory_usage_used'])+"K used  "+str(self.sysReso_response['memory_usage_free'])+"K free"))
        item = self.listWidget_4.item(4)
        item.setText(_translate("form_2", "Current memory status: "+str(self.sysReso_response['current_memory_status'])))
        
        
        
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.pushButton_7.setText(_translate("form_2", "查   看"))
        self.pushButton_8.setText(_translate("form_2", "查   看"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        
        routes=str(self.ip_route_response['routes'])
        paths=str(self.ip_route_response['paths'])
        item = self.listWidget_2.item(0)
        item.setText(_translate("form_2", "Total number of routes:  "+routes))
        item = self.listWidget_2.item(1)
        item.setText(_translate("form_2", "Total number of paths:  "+paths))
        item = self.listWidget_2.item(2)
        item.setText(_translate("form_2", "mask_length                route_count"))
        
        
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        
        
        result=str(self.proc_log_response['result'])
        item = self.listWidget_3.item(0)
        item.setText(_translate("form_2", "result:  "+ result))
        
        
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.pushButton_5.setText(_translate("form_2", "查   看"))
        self.label_9.setText(_translate("form_2", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">路由</span></p><p align=\"center\"><span style=\" font-size:10pt;\">摘要</span></p></body></html>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
        administrative=self.redundancy_response['rdn_mode_admin']
        operational=self.redundancy_response['rdn_mode_oper']
        supervisor=self.redundancy_response['this_sup']
        Redundancy=self.redundancy_response['this_sup_rdn_state']
        Supervisor=self.redundancy_response['this_sup_sup_state']
        Internal=self.redundancy_response['this_sup_internal_state']
        item = self.listWidget.item(0)
        item.setText(_translate("form_2", "adminstrative:  "+administrative))
        item = self.listWidget.item(1)
        item.setText(_translate("form_2", "operational:  "+operational))
        item = self.listWidget.item(2)
        item.setText(_translate("form_2", "This supervisor:  "+supervisor))
        item = self.listWidget.item(3)
        item.setText(_translate("form_2", "Redundancy state:  "+Redundancy))
        item = self.listWidget.item(4)
        item.setText(_translate("form_2", "Supervisor state:  "+Supervisor))
        item = self.listWidget.item(5)
        item.setText(_translate("form_2", "Internal state:  "+Internal))
        
        
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("form_2", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">平台内存</span></p><p align=\"center\"><span style=\" font-size:10pt;\">统计信息</span></p></body></html>"))
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_form_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
