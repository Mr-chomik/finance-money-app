import sys

import pyqtgraph as pg
from pycbrf.toolbox import ExchangeRates
from datetime import datetime, date, timedelta
from pyqtgraph import PlotWidget
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


class Ui_MainWindow_currency(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 390)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(680, 20, 391, 261))
        self.graphicsView.setStyleSheet("border-color: rgb(232, 232, 232);\n"
                                        "background-color: rgb(117, 117, 117);")
        self.graphicsView.setObjectName("graphicsView")
        self.currency_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.currency_table.setGeometry(QtCore.QRect(10, 10, 661, 271))
        self.currency_table.setStyleSheet("background-color: rgb(200, 200, 200);\n"
                                          "color: rgb(0, 0, 0);")
        self.currency_table.setObjectName("currency_table")
        self.currency_table.setColumnCount(5)
        self.currency_table.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.currency_table.setItem(7, 0, item)
        self.drawer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.drawer.setGeometry(QtCore.QRect(940, 300, 131, 38))
        self.drawer.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "font: 25 16pt \"Segoe UI Light\";")
        self.drawer.setObjectName("drawer")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(690, 290, 236, 27))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.weekBox = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.weekBox.setStyleSheet("font: 15pt \"GOST type A\";\n"
                                   "color: rgb(255, 255, 255);")
        self.weekBox.setChecked(True)
        self.weekBox.setObjectName("weekBox")
        self.horizontalLayout.addWidget(self.weekBox)
        self.monthBox = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.monthBox.setStyleSheet("font: 15pt \"GOST type A\";\n"
                                    "color: rgb(255, 255, 255);")
        self.monthBox.setObjectName("monthBox")
        self.horizontalLayout.addWidget(self.monthBox)
        self.yearBox = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.yearBox.setStyleSheet("font: 15pt \"GOST type A\";\n"
                                   "color: rgb(255, 255, 255);")
        self.yearBox.setObjectName("yearBox")
        self.horizontalLayout.addWidget(self.yearBox)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(690, 320, 241, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.eur = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.eur.setStyleSheet("font: 12pt \"GOST type A\";\n"
                               "color: rgb(255, 255, 255);")
        self.eur.setObjectName("eur")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.eur)
        self.gridLayout.addWidget(self.eur, 0, 2, 1, 1)
        self.cny = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.cny.setStyleSheet("font: 12pt \"GOST type A\";\n"
                               "color: rgb(255, 255, 255);")
        self.cny.setObjectName("cny")
        self.buttonGroup.addButton(self.cny)
        self.gridLayout.addWidget(self.cny, 0, 1, 1, 1)
        self.rub = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.rub.setStyleSheet("font: 12pt \"GOST type A\";\n"
                               "color: rgb(255, 255, 255);")
        self.rub.setChecked(True)
        self.rub.setObjectName("rub")
        self.buttonGroup.addButton(self.rub)
        self.gridLayout.addWidget(self.rub, 0, 0, 1, 1)
        self.pln = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.pln.setStyleSheet("font: 12pt \"GOST type A\";\n"
                               "color: rgb(255, 255, 255);")
        self.pln.setObjectName("pln")
        self.buttonGroup.addButton(self.pln)
        self.gridLayout.addWidget(self.pln, 1, 3, 1, 1)
        self.kzt = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.kzt.setStyleSheet("font: 16pt \"GOST type A\";\n"
                               "color: rgb(255, 255, 255);")
        self.kzt.setObjectName("kzt")
        self.buttonGroup.addButton(self.kzt)
        self.gridLayout.addWidget(self.kzt, 1, 2, 1, 1)
        self.inr = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.inr.setStyleSheet("font: 12pt \"GOST type A\";\n"
                               "color: rgb(255, 255, 255);")
        self.inr.setObjectName("inr")
        self.buttonGroup.addButton(self.inr)
        self.gridLayout.addWidget(self.inr, 1, 1, 1, 1)
        self.Try = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.Try.setStyleSheet("font: 12pt \"GOST type A\";\n"
                               "color: rgb(255, 255, 255);")
        self.Try.setObjectName("Try")
        self.buttonGroup.addButton(self.Try)
        self.gridLayout.addWidget(self.Try, 1, 0, 1, 1)
        self.gbp = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.gbp.setStyleSheet("font: 12pt \"GOST type A\";\n"
                               "color: rgb(255, 255, 255);")
        self.gbp.setObjectName("gbp")
        self.buttonGroup.addButton(self.gbp)
        self.gridLayout.addWidget(self.gbp, 0, 3, 1, 1)
        self.calc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calc.setGeometry(QtCore.QRect(30, 310, 201, 27))
        self.calc.setStyleSheet("color: rgb(0, 0, 0);\n"
                                "background-color: rgb(218, 218, 218);\n"
                                "font: italic 12pt \"MS Sans Serif\";")
        self.calc.setObjectName("calc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.currency_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "$"))
        item = self.currency_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "¥"))
        item = self.currency_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "€"))
        item = self.currency_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "£"))
        item = self.currency_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "₺"))
        item = self.currency_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "₹"))
        item = self.currency_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "₸"))
        item = self.currency_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "zł"))
        item = self.currency_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Валюта"))
        item = self.currency_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.currency_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Изменение цены за день"))
        item = self.currency_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Изменение цены за неделю"))
        item = self.currency_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Изменение цены за месяц"))
        __sortingEnabled = self.currency_table.isSortingEnabled()
        self.currency_table.setSortingEnabled(False)
        item = self.currency_table.item(0, 0)
        item.setText(_translate("MainWindow", "Доллар USD"))
        item = self.currency_table.item(1, 0)
        item.setText(_translate("MainWindow", "Юань CNY"))
        item = self.currency_table.item(2, 0)
        item.setText(_translate("MainWindow", "Евро EUR"))
        item = self.currency_table.item(3, 0)
        item.setText(_translate("MainWindow", "Фунт GBP"))
        item = self.currency_table.item(4, 0)
        item.setText(_translate("MainWindow", "Лира TRY"))
        item = self.currency_table.item(5, 0)
        item.setText(_translate("MainWindow", "Рупия INR"))
        item = self.currency_table.item(6, 0)
        item.setText(_translate("MainWindow", "Тенге KZT"))
        item = self.currency_table.item(7, 0)
        item.setText(_translate("MainWindow", "Злотый PLN"))
        self.currency_table.setSortingEnabled(__sortingEnabled)
        self.drawer.setText(_translate("MainWindow", "Построить"))
        self.weekBox.setText(_translate("MainWindow", "Неделя"))
        self.monthBox.setText(_translate("MainWindow", "Месяц"))
        self.yearBox.setText(_translate("MainWindow", "Квартал"))
        self.eur.setText(_translate("MainWindow", "€"))
        self.cny.setText(_translate("MainWindow", "¥"))
        self.rub.setText(_translate("MainWindow", "$"))
        self.pln.setText(_translate("MainWindow", "zł"))
        self.kzt.setText(_translate("MainWindow", "₸"))
        self.inr.setText(_translate("MainWindow", "₹"))
        self.Try.setText(_translate("MainWindow", "₺"))
        self.gbp.setText(_translate("MainWindow", "£"))
        self.calc.setText(_translate("MainWindow", "Калькулятор валют"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.currency_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "$"))
        item = self.currency_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "¥"))
        item = self.currency_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "€"))
        item = self.currency_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "£"))
        item = self.currency_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "₺"))
        item = self.currency_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "₹"))
        item = self.currency_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "₸"))
        item = self.currency_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "zł"))
        item = self.currency_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Валюта"))
        item = self.currency_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.currency_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Изменение цены за день"))
        item = self.currency_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Изменение цены за неделю"))
        item = self.currency_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Изменение цены за месяц"))
        __sortingEnabled = self.currency_table.isSortingEnabled()
        self.currency_table.setSortingEnabled(False)
        item = self.currency_table.item(0, 0)
        item.setText(_translate("MainWindow", "Доллар USD"))
        item = self.currency_table.item(1, 0)
        item.setText(_translate("MainWindow", "Юань CNY"))
        item = self.currency_table.item(2, 0)
        item.setText(_translate("MainWindow", "Евро EUR"))
        item = self.currency_table.item(3, 0)
        item.setText(_translate("MainWindow", "Фунт GBP"))
        item = self.currency_table.item(4, 0)
        item.setText(_translate("MainWindow", "Лира TRY"))
        item = self.currency_table.item(5, 0)
        item.setText(_translate("MainWindow", "Рупия INR"))
        item = self.currency_table.item(6, 0)
        item.setText(_translate("MainWindow", "Тенге KZT"))
        item = self.currency_table.item(7, 0)
        item.setText(_translate("MainWindow", "Злотый PLN"))
        self.currency_table.setSortingEnabled(__sortingEnabled)
        self.drawer.setText(_translate("MainWindow", "Построить"))
        self.weekBox.setText(_translate("MainWindow", "Неделя"))
        self.monthBox.setText(_translate("MainWindow", "Месяц"))
        self.yearBox.setText(_translate("MainWindow", "Квартал"))
        self.eur.setText(_translate("MainWindow", "€"))
        self.cny.setText(_translate("MainWindow", "¥"))
        self.rub.setText(_translate("MainWindow", "$"))
        self.pln.setText(_translate("MainWindow", "zł"))
        self.kzt.setText(_translate("MainWindow", "₸"))
        self.inr.setText(_translate("MainWindow", "₹"))
        self.Try.setText(_translate("MainWindow", "₺"))
        self.gbp.setText(_translate("MainWindow", "£"))
        self.calc.setText(_translate("MainWindow", "Калькулятор валют"))


class Ui_MainWindow_currency_calc(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 175)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ToCount = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ToCount.setGeometry(QtCore.QRect(160, 110, 111, 39))
        self.ToCount.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "font: 25 14pt \"Segoe UI Light\";")
        self.ToCount.setObjectName("ToCount")
        self.currBox_1 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.currBox_1.setGeometry(QtCore.QRect(30, 20, 101, 22))
        self.currBox_1.setStyleSheet("background-color: rgb(120, 120, 120);\n"
                                     "color: rgb(0, 0, 0);")
        self.currBox_1.setObjectName("currBox_1")
        self.currBox_1.addItem("")
        self.currBox_1.addItem("")
        self.currBox_1.addItem("")
        self.currBox_1.addItem("")
        self.currBox_1.addItem("")
        self.currBox_1.addItem("")
        self.currBox_1.addItem("")
        self.currBox_1.addItem("")
        self.currBox_1.addItem("")
        self.currBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.currBox_2.setGeometry(QtCore.QRect(290, 20, 101, 22))
        self.currBox_2.setStyleSheet("background-color: rgb(120, 120, 120);\n"
                                     "color: rgb(0, 0, 0);")
        self.currBox_2.setObjectName("currBox_2")
        self.currBox_2.addItem("")
        self.currBox_2.addItem("")
        self.currBox_2.addItem("")
        self.currBox_2.addItem("")
        self.currBox_2.addItem("")
        self.currBox_2.addItem("")
        self.currBox_2.addItem("")
        self.currBox_2.addItem("")
        self.currBox_2.addItem("")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(156, 50, 111, 51))
        self.label.setStyleSheet("background-color: rgb(65, 65, 65);\n"
                                 "font: 42pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.first_count = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.first_count.setGeometry(QtCore.QRect(20, 60, 121, 41))
        self.first_count.setStyleSheet("background-color: rgb(200, 200, 200);\n"
                                       "color: rgb(0, 0, 0);")
        self.first_count.setObjectName("first_count")
        self.second_count = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.second_count.setGeometry(QtCore.QRect(280, 60, 121, 41))
        self.second_count.setStyleSheet("background-color: rgb(200, 200, 200);\n"
                                        "color: rgb(0, 0, 0);")
        self.second_count.setObjectName("second_count")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ToCount.setText(_translate("MainWindow", "Посчитать"))
        self.currBox_1.setItemText(0, _translate("MainWindow", "USD"))
        self.currBox_1.setItemText(1, _translate("MainWindow", "RUB"))
        self.currBox_1.setItemText(2, _translate("MainWindow", "CNY"))
        self.currBox_1.setItemText(3, _translate("MainWindow", "EUR"))
        self.currBox_1.setItemText(4, _translate("MainWindow", "GBP"))
        self.currBox_1.setItemText(5, _translate("MainWindow", "TRY"))
        self.currBox_1.setItemText(6, _translate("MainWindow", "INR"))
        self.currBox_1.setItemText(7, _translate("MainWindow", "KZT"))
        self.currBox_1.setItemText(8, _translate("MainWindow", "PLN"))
        self.currBox_2.setItemText(0, _translate("MainWindow", "RUB"))
        self.currBox_2.setItemText(1, _translate("MainWindow", "USD"))
        self.currBox_2.setItemText(2, _translate("MainWindow", "CNY"))
        self.currBox_2.setItemText(3, _translate("MainWindow", "EUR"))
        self.currBox_2.setItemText(4, _translate("MainWindow", "GBP"))
        self.currBox_2.setItemText(5, _translate("MainWindow", "TRY"))
        self.currBox_2.setItemText(6, _translate("MainWindow", "INR"))
        self.currBox_2.setItemText(7, _translate("MainWindow", "KZT"))
        self.currBox_2.setItemText(8, _translate("MainWindow", "PLN"))
        self.label.setText(_translate("MainWindow", "  ⇄"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ToCount.setText(_translate("MainWindow", "Посчитать"))
        self.currBox_1.setItemText(0, _translate("MainWindow", "USD"))
        self.currBox_1.setItemText(1, _translate("MainWindow", "RUB"))
        self.currBox_1.setItemText(2, _translate("MainWindow", "CNY"))
        self.currBox_1.setItemText(3, _translate("MainWindow", "EUR"))
        self.currBox_1.setItemText(4, _translate("MainWindow", "GBP"))
        self.currBox_1.setItemText(5, _translate("MainWindow", "TRY"))
        self.currBox_1.setItemText(6, _translate("MainWindow", "INR"))
        self.currBox_1.setItemText(7, _translate("MainWindow", "KZT"))
        self.currBox_1.setItemText(8, _translate("MainWindow", "PLN"))
        self.currBox_2.setItemText(0, _translate("MainWindow", "RUB"))
        self.currBox_2.setItemText(1, _translate("MainWindow", "USD"))
        self.currBox_2.setItemText(2, _translate("MainWindow", "CNY"))
        self.currBox_2.setItemText(3, _translate("MainWindow", "EUR"))
        self.currBox_2.setItemText(4, _translate("MainWindow", "GBP"))
        self.currBox_2.setItemText(5, _translate("MainWindow", "TRY"))
        self.currBox_2.setItemText(6, _translate("MainWindow", "INR"))
        self.currBox_2.setItemText(7, _translate("MainWindow", "KZT"))
        self.currBox_2.setItemText(8, _translate("MainWindow", "PLN"))
        self.label.setText(_translate("MainWindow", "  ⇄"))


class Currency_form(QMainWindow, Ui_MainWindow_currency):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Валюты')
        self.currency_table.resizeColumnsToContents()
        self.d = {"$": "USD",
             "¥": "CNY",
             "€": "EUR",
             "£": "GBP",
             "₺": "TRY",
             "₹": "INR",
             "₸": "KZT",
             "zł": "PLN",
                  }

        for i in range(1, 5):
            for j, curr in enumerate(self.d.values()):
                rates = ExchangeRates(date.today())
                now = round(rates[curr].value, 2)
                if i == 1:
                    self.currency_table.setItem(j, i, QTableWidgetItem(f"{now}"))
                elif i == 2:
                    rates = ExchangeRates(date.today() - timedelta(1))
                    past = round(rates[curr].value, 2)
                    changes = round(((now - past) / past) * 100, 2)
                    self.currency_table.setItem(j, i, QTableWidgetItem(f"{changes}%"))
                elif i == 3:
                    rates = ExchangeRates(date.today() - timedelta(7))
                    past = round(rates[curr].value, 2)
                    changes = round(((now - past) / past) * 100, 2)
                    self.currency_table.setItem(j, i, QTableWidgetItem(f"{changes}%"))
                elif i == 4:
                    rates = ExchangeRates(date.today() - timedelta(30))
                    past = round(rates[curr].value, 2)
                    changes = round(((now - past) / past) * 100, 2)
                    self.currency_table.setItem(j, i, QTableWidgetItem(f"{changes}%"))

        self.drawer.clicked.connect(self.draw)
        self.calc.clicked.connect(self.calc_open)

    def draw(self):
        self.graphicsView.clear()
        for button in self.buttonGroup.buttons():
            if button.isChecked():
                curr = self.d[button.text()]

        if self.weekBox.isChecked():
            dates = []
            currs = []
            last, start = 0, 0
            pen = ""
            for i in range(7, -1, -1):
                if i == 0:
                    rates = ExchangeRates(str(date.today()))
                    dates.append(str(date.today()))
                    last = round(rates[curr].value, 2)
                else:
                    rates = ExchangeRates(date.today() - timedelta(i))
                    dates.append(str(date.today() - timedelta(i)))
                if i == 7:
                    start = round(rates[curr].value, 2)
                currs.append(round(rates[curr].value, 2))
            if start < last:
                pen = pg.mkPen(color=(0, 255, 0), width=1.5)
            elif start == last:
                pen = pg.mkPen(color=(255, 255, 0), width=1.5)
            else:
                pen = pg.mkPen(color=(255, 0, 0), width=1.5)

        elif self.monthBox.isChecked():
            dates = []
            currs = []
            last = 0
            start = 0
            pen = ""
            for i in range(30, -1, -1):
                if i == 0:
                    rates = ExchangeRates(str(date.today()))
                    dates.append(str(date.today()))
                    last = round(rates[curr].value, 2)
                else:
                    rates = ExchangeRates(date.today() - timedelta(i))
                    dates.append(str(date.today() - timedelta(i)))
                if i == 30:
                    start = round(rates[curr].value, 2)
                currs.append(round(rates[curr].value, 2))

            if start < last:
                pen = pg.mkPen(color=(0, 255, 0), width=1.5)
            elif start == last:
                pen = pg.mkPen(color=(255, 255, 0), width=1.5)
            else:
                pen = pg.mkPen(color=(255, 0, 0), width=1.5)

        if self.yearBox.isChecked():
            dates = []
            currs = []
            last, start = 0, 0
            pen = ""
            for i in range(90, -1, -1):
                if i == 0:
                    rates = ExchangeRates(str(date.today()))
                    dates.append(str(date.today()))
                    last = round(rates[curr].value, 2)
                else:
                    rates = ExchangeRates(date.today() - timedelta(i))
                    dates.append(str(date.today() - timedelta(i)))
                if i == 90:
                    start = round(rates[curr].value, 2)
                currs.append(round(rates[curr].value, 2))
            if start < last:
                pen = pg.mkPen(color=(0, 255, 0), width=1.5)
            elif start == last:
                pen = pg.mkPen(color=(255, 255, 0), width=1.5)
            else:
                pen = pg.mkPen(color=(255, 0, 0), width=1.5)

        self.x, self.y = [], []
        for x in dates:
            self.x.append(datetime.strptime(x, '%Y-%m-%d'))

        for y in currs:
            self.y.append(float(y))

        self.graphicsView.showGrid(x=True, y=True)
        self.graphicsView.plot(
            x=[x.timestamp() for x in self.x],
            y=self.y, pen=pen, symbol="o", symbolSize=3.25, symbolBrush="w")

    def calc_open(self):
        self.Currency_calc_form = Currency_calc_form()
        self.Currency_calc_form.show()

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_H:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Помощь в валютах")
                dlg.setText("""Для построения графика валюты: 
1)Выберите временной промежуток и желаемую валюту.
2)Нажмите кнопку 'Построить'.
В зависимости от временного промежутка построение займет 1-5 секунд

Для перевода валют из одной в другую перейдите в калькулятор валют
по соответсвующей кнопке""")
                dlg.exec()


class Currency_calc_form(QMainWindow, Ui_MainWindow_currency_calc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Калькулятор валют')
        self.ToCount.clicked.connect(self.count)
        self.second_count.setReadOnly(True)

    def count(self):
        rates = ExchangeRates(str(date.today()))
        result = ""
        if self.currBox_1.currentText() == self.currBox_2.currentText():
            result = f"{self.first_count.text()}"

        elif self.currBox_1.currentText() == "RUB":
            result = f"{round(float(self.first_count.text()) / float(rates[self.currBox_2.currentText()].value), 2)}"

        elif self.currBox_2.currentText() == "RUB":
            result = f"{round(float(rates[self.currBox_1.currentText()].value) * float(self.first_count.text()), 2)}"

        else:
            result = f"""{round(float(rates[self.currBox_1.currentText()].value) * float(self.first_count.text())
                                / float(rates[self.currBox_2.currentText()].value), 2)}"""

        if self.currBox_1.currentText() != self.currBox_2.currentText():
            if result.split(".")[1][0] == "0":
                result = result.split(".")[0]

        self.second_count.setText(result)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_H:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Помощь в калькуляторе валют")
                dlg.setText("""Выберите валюты для обмена.
Введите в первую ячейку сумму(в выбранной валюте) для перевода в выбранную валюту.
Нажмите 'Посчитать'

В качестве разделителя используйте строго ' . ' (точку)""")
                dlg.exec()