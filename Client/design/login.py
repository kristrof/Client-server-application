# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\trofi\PycharmProjects\client\venv\Scripts\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets

class Ui_Client_main(object):
    def setupUi(self, Client_main):
        Client_main.setObjectName("Client_main")
        Client_main.resize(356, 327)
        self.centralwidget = QtWidgets.QWidget(Client_main)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 180, 321, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 30, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        Client_main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Client_main)
        self.statusbar.setObjectName("statusbar")
        Client_main.setStatusBar(self.statusbar)

        self.retranslateUi(Client_main)
        QtCore.QMetaObject.connectSlotsByName(Client_main)

    def retranslateUi(self, Client_main):
        _translate = QtCore.QCoreApplication.translate
        Client_main.setWindowTitle(_translate("Client_main", "Client"))
        self.label.setText(_translate("Client_main", "Логин:"))
        self.label_2.setText(_translate("Client_main", "Пароль"))
        self.pushButton.setText(_translate("Client_main", "Войти"))
        self.label_3.setText(_translate("Client_main", "Вход"))

