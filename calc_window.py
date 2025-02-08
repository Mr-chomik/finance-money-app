import sys, math


from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QMessageBox


class Ui_Form_calc(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(375, 515)
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 345, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QLCDNumber(parent=self.layoutWidget)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn8 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn8.setMinimumSize(QtCore.QSize(80, 80))
        self.btn8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.buttonGroup_digits = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_digits.setObjectName("buttonGroup_digits")
        self.buttonGroup_digits.addButton(self.btn8)
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn2.setMinimumSize(QtCore.QSize(80, 80))
        self.btn2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.buttonGroup_digits.addButton(self.btn2)
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_plus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_plus.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.buttonGroup_binary = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_binary.setObjectName("buttonGroup_binary")
        self.buttonGroup_binary.addButton(self.btn_plus)
        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_eq.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_eq.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_eq.setFont(font)
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout.addWidget(self.btn_eq, 3, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn0.setMinimumSize(QtCore.QSize(80, 80))
        self.btn0.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.buttonGroup_digits.addButton(self.btn0)
        self.gridLayout.addWidget(self.btn0, 3, 0, 1, 1)
        self.btn_div = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_div.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_div.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.buttonGroup_binary.addButton(self.btn_div)
        self.gridLayout.addWidget(self.btn_div, 3, 3, 1, 1)
        self.btn1 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn1.setMinimumSize(QtCore.QSize(80, 80))
        self.btn1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.buttonGroup_digits.addButton(self.btn1)
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn9.setMinimumSize(QtCore.QSize(80, 80))
        self.btn9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.buttonGroup_digits.addButton(self.btn9)
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_dot.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_dot.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 3, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn3.setMinimumSize(QtCore.QSize(80, 80))
        self.btn3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.buttonGroup_digits.addButton(self.btn3)
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn4.setMinimumSize(QtCore.QSize(80, 80))
        self.btn4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.buttonGroup_digits.addButton(self.btn4)
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn5.setMinimumSize(QtCore.QSize(80, 80))
        self.btn5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.buttonGroup_digits.addButton(self.btn5)
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn7 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn7.setMinimumSize(QtCore.QSize(80, 80))
        self.btn7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.buttonGroup_digits.addButton(self.btn7)
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn6.setMinimumSize(QtCore.QSize(80, 80))
        self.btn6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.buttonGroup_digits.addButton(self.btn6)
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_minus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_minus.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.buttonGroup_binary.addButton(self.btn_minus)
        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_mult.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_mult.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.buttonGroup_binary.addButton(self.btn_mult)
        self.gridLayout.addWidget(self.btn_mult, 2, 3, 1, 1)
        self.btn_pow = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_pow.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_pow.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_pow.setFont(font)
        self.btn_pow.setObjectName("btn_pow")
        self.buttonGroup_binary.addButton(self.btn_pow)
        self.gridLayout.addWidget(self.btn_pow, 4, 0, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_sqrt.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_sqrt.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout.addWidget(self.btn_sqrt, 4, 1, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_fact.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_fact.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_fact.setFont(font)
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout.addWidget(self.btn_fact, 4, 2, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_clear.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(254, 166, 43);")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Красивый калькулятор"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn_plus.setText(_translate("Form", "+"))
        self.btn_eq.setText(_translate("Form", "="))
        self.btn0.setText(_translate("Form", "0"))
        self.btn_div.setText(_translate("Form", "/"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn_dot.setText(_translate("Form", "."))
        self.btn3.setText(_translate("Form", "3"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn_minus.setText(_translate("Form", "-"))
        self.btn_mult.setText(_translate("Form", "*"))
        self.btn_pow.setText(_translate("Form", "^"))
        self.btn_sqrt.setText(_translate("Form", "√"))
        self.btn_fact.setText(_translate("Form", "!"))
        self.btn_clear.setText(_translate("Form", "С"))


class Calculator_form(QMainWindow, Ui_Form_calc):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Калькулятор')
        self.first = "0"
        self.second = ""
        self.value = ""
        self.result = "0"
        for button in self.buttonGroup_digits.buttons():
            button.clicked.connect(self.digits)
        for button in self.buttonGroup_binary.buttons():
            button.clicked.connect(self.binary)
        self.btn_clear.clicked.connect(self.run)
        self.btn_fact.clicked.connect(self.run)
        self.btn_sqrt.clicked.connect(self.run)
        self.btn_eq.clicked.connect(self.run)
        self.btn_dot.clicked.connect(self.run)

    def run(self):
        if self.sender().text() == ".":
            if self.first == "":
                self.first = "0."
                self.table.display(self.first)
            elif self.first != "" and self.second == "":
                self.first += "."
                self.table.display(self.first)
            else:
                self.second += "."
                self.table.display(self.second)

        elif self.sender().text() == self.btn_clear.text():
            self.table.display("0")
            self.first = "0"
            self.second = ""
            self.value = ""

        elif self.sender().text() == self.btn_eq.text():
            if self.value == "/" and self.second == "0":
                self.table.display("Error")
                self.first = "0"
            else:
                self.result = eval(f"{self.first} {self.value} {self.second}")
                if "." in str(self.result):
                    self.result = round(self.result, 1)
                self.table.display(self.result)
                self.first = self.result
            self.second = ""
            self.value = ""
            self.result = "0"

        elif self.sender().text() == self.btn_fact.text():
            self.table.display(str(round(math.factorial(int(self.first)), 1)))
            self.first = str(math.factorial(int(self.first)))
            self.second = ""
            self.value = ""

        elif self.sender().text() == self.btn_sqrt.text():
            if self.first < 0:
                self.table.display("Error")
                self.first = "0"
            else:
                self.table.display(str(round(math.sqrt(int(self.first)), 1)))
                self.first = str(math.sqrt(int(self.first)))
            self.second = ""
            self.value = ""

    def digits(self):
        if self.value == "" or self.first == "-":
            if self.first == "-":
                self.first += self.sender().text()
                self.table.display("0" + self.first)
            elif self.first != "0":
                self.first += self.sender().text()
                self.table.display(self.first)
            else:
                self.first = self.sender().text()
                self.table.display(self.first)

        else:
            self.second += self.sender().text()
            self.table.display(self.second)

    def binary(self):
        if self.sender().text() == "-" and self.first == "0":
            self.value = "-"
            self.table.display(self.first + self.value)
        elif self.sender().text() == "^":
            self.value = "**"
        else:
            self.value = self.sender().text()

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_H:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Помощь в калькуляторе")
                dlg.setText("""Обычный калькулятор, ничего интересного

В случае неполадки нажмите 'C' или перезапустите окно""")
                dlg.exec()