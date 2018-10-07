# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_ui.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 191, 17))
        self.label.setObjectName("label")
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(250, 130, 171, 21))
        self.Button.setObjectName("Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.twitter_name = QtWidgets.QLineEdit(self.centralwidget)
        self.twitter_name.setGeometry(QtCore.QRect(290, 80, 241, 27))
        self.twitter_name.setObjectName("twitter_name")
        self.resultWindow = QtWidgets.QLabel(self.centralwidget)
        self.resultWindow.setGeometry(QtCore.QRect(90, 160, 491, 71))
        self.resultWindow.setText("")
        self.resultWindow.setObjectName("resultWindow")
        self.YesButton = QtWidgets.QPushButton(self.centralwidget)
        self.YesButton.setGeometry(QtCore.QRect(320, 260, 99, 27))
        self.YesButton.setObjectName("YesButton")
        self.NoButton = QtWidgets.QPushButton(self.centralwidget)
        self.NoButton.setGeometry(QtCore.QRect(470, 260, 99, 27))
        self.NoButton.setObjectName("NoButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 251, 20))
        self.label_3.setObjectName("label_3")
        self.resultWindow2 = QtWidgets.QLabel(self.centralwidget)
        self.resultWindow2.setGeometry(QtCore.QRect(117, 360, 461, 191))
        self.resultWindow2.setText("")
        self.resultWindow2.setObjectName("resultWindow2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SHADE APP"))
        self.label.setText(_translate("MainWindow", "Enter your Twitter handle:"))
        self.Button.setText(_translate("MainWindow", "Know your mood"))
        self.label_2.setText(_translate("MainWindow", "SHADE APP"))
        self.YesButton.setText(_translate("MainWindow", "Yes"))
        self.NoButton.setText(_translate("MainWindow", "No"))
        self.label_3.setText(_translate("MainWindow", "Do you have an account on Spotify?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

