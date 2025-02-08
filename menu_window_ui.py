import sys


from PyQt6 import QtWidgets, QtCore


class Ui_MainWindow_menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 440)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.currency = QtWidgets.QPushButton(parent=self.centralwidget)
        self.currency.setGeometry(QtCore.QRect(100, 50, 171, 121))
        self.currency.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 17pt \"Book Antiqua\";")
        self.currency.setObjectName("currency")
        self.calculator = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculator.setGeometry(QtCore.QRect(400, 50, 171, 121))
        self.calculator.setStyleSheet("font: 16pt \"Book Antiqua\";\n"
                                      "background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);")
        self.calculator.setObjectName("calculator")
        self.equation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equation.setGeometry(QtCore.QRect(100, 240, 171, 121))
        self.equation.setStyleSheet("font: 17pt \"Book Antiqua\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(0, 0, 0);")
        self.equation.setObjectName("equation")
        self.graph = QtWidgets.QPushButton(parent=self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(400, 240, 171, 121))
        self.graph.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "font: 17pt \"Book Antiqua\";\n"
                                 "color: rgb(255, 255, 255);")
        self.graph.setObjectName("graph")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 400, 141, 16))
        self.label.setStyleSheet("color: rgb(150, 150, 150);\n"
                                 "font: 8pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.currency.setText(_translate("MainWindow", "Валюты"))
        self.calculator.setText(_translate("MainWindow", "Калькулятор"))
        self.equation.setText(_translate("MainWindow", "Уравнения\n"
                                                       "Неравенства"))
        self.graph.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p align=\"justify\">Графики</p></body></html>"))
        self.graph.setText(_translate("MainWindow", "Графики"))
        self.label.setText(_translate("MainWindow", "Для помощи - Ctrl+H"))