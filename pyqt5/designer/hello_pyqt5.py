# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello_pyqt5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 220, 111, 71))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 340, 112, 34))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuPyqt5 = QtWidgets.QMenu(self.menubar)
        self.menuPyqt5.setObjectName("menuPyqt5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionxixi = QtWidgets.QAction(MainWindow)
        self.actionxixi.setObjectName("actionxixi")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionnew_2 = QtWidgets.QAction(MainWindow)
        self.actionnew_2.setObjectName("actionnew_2")
        self.actionsave_2 = QtWidgets.QAction(MainWindow)
        self.actionsave_2.setObjectName("actionsave_2")
        self.menuPyqt5.addAction(self.actionxixi)
        self.menuPyqt5.addSeparator()
        self.menuPyqt5.addAction(self.actionnew_2)
        self.menuPyqt5.addSeparator()
        self.menuPyqt5.addAction(self.actionsave_2)
        self.menubar.addAction(self.menuPyqt5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HelloPyqt5"))
        self.label.setText(_translate("MainWindow", "HelloPyqt5"))
        self.pushButton.setText(_translate("MainWindow", "Button"))
        self.menuPyqt5.setTitle(_translate("MainWindow", "File"))
        self.actionxixi.setText(_translate("MainWindow", "open"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionnew_2.setText(_translate("MainWindow", "new"))
        self.actionsave_2.setText(_translate("MainWindow", "save"))

