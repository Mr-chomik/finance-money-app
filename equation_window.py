import sys

from math import sqrt
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class Ui_MainWindow_equation(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 402)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.equation = QtWidgets.QLabel(parent=self.centralwidget)
        self.equation.setGeometry(QtCore.QRect(220, 10, 241, 35))
        self.equation.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(0,0,0);\n"
                                    "background-color: rgb(210, 210, 210);")
        self.equation.setObjectName("equation")
        self.discriminant = QtWidgets.QLabel(parent=self.centralwidget)
        self.discriminant.setGeometry(QtCore.QRect(250, 60, 161, 33))
        self.discriminant.setStyleSheet("font: 17pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0,0,0);\n"
                                        "background-color: rgb(210, 210, 210);")
        self.discriminant.setObjectName("discriminant")
        self.firstAnswer = QtWidgets.QLabel(parent=self.centralwidget)
        self.firstAnswer.setGeometry(QtCore.QRect(260, 110, 141, 33))
        self.firstAnswer.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(0,0,0);\n"
                                       "background-color: rgb(210, 210, 210);")
        self.firstAnswer.setObjectName("firstAnswer")
        self.secondAnswer = QtWidgets.QLabel(parent=self.centralwidget)
        self.secondAnswer.setGeometry(QtCore.QRect(260, 160, 141, 33))
        self.secondAnswer.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0,0,0);\n"
                                        "background-color: rgb(210, 210, 210);")
        self.secondAnswer.setObjectName("secondAnswer")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 77))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quadratic = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.quadratic.setStyleSheet("font: 12pt \"GOST type A\";\n"
                                     "color: rgb(255, 255, 255);")
        self.quadratic.setChecked(True)
        self.quadratic.setObjectName("quadratic")
        self.verticalLayout_2.addWidget(self.quadratic)
        self.biquadratic = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.biquadratic.setStyleSheet("font: 12pt \"GOST type A\";\n"
                                       "color: rgb(255, 255, 255);")
        self.biquadratic.setChecked(False)
        self.biquadratic.setObjectName("biquadratic")
        self.verticalLayout_2.addWidget(self.biquadratic)
        self.inequality = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.inequality.setStyleSheet("font: 12pt \"GOST type A\";\n"
                                      "color: rgb(255, 255, 255);")
        self.inequality.setObjectName("inequality")
        self.verticalLayout_2.addWidget(self.inequality)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 200, 171, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.secondLab = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.secondLab.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 12pt \"MS Shell Dlg 2\";")
        self.secondLab.setObjectName("secondLab")
        self.gridLayout.addWidget(self.secondLab, 1, 0, 1, 1)
        self.firstLab = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.firstLab.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.firstLab.setObjectName("firstLab")
        self.gridLayout.addWidget(self.firstLab, 0, 0, 1, 1)
        self.thirdLab = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.thirdLab.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.thirdLab.setObjectName("thirdLab")
        self.gridLayout.addWidget(self.thirdLab, 2, 0, 1, 1)
        self.thirdBox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.thirdBox.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.thirdBox.setObjectName("thirdBox")
        self.gridLayout.addWidget(self.thirdBox, 2, 1, 1, 1)
        self.secondBox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.secondBox.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 12pt \"MS Shell Dlg 2\";")
        self.secondBox.setObjectName("secondBox")
        self.gridLayout.addWidget(self.secondBox, 1, 1, 1, 1)
        self.firstBox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.firstBox.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.firstBox.setObjectName("firstBox")
        self.gridLayout.addWidget(self.firstBox, 0, 1, 1, 1)
        self.starter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.starter.setGeometry(QtCore.QRect(280, 300, 101, 31))
        self.starter.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "font: 25 16pt \"Segoe UI Light\";")
        self.starter.setObjectName("starter")
        self.uploadBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.uploadBtn.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.uploadBtn.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "font: 12pt \"Times New Roman\";")
        self.uploadBtn.setObjectName("uploadBtn")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 121, 110))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.less = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.less.setStyleSheet("font: 12pt \"GOST type A\";\n"
                                "color: rgb(255, 255, 255);")
        self.less.setChecked(True)
        self.less.setObjectName("less")
        self.verticalLayout_3.addWidget(self.less)
        self.more = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.more.setStyleSheet("font: 12pt \"GOST type A\";\n"
                                "color: rgb(255, 255, 255);")
        self.more.setChecked(False)
        self.more.setObjectName("more")
        self.verticalLayout_3.addWidget(self.more)
        self.lessEqual = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.lessEqual.setStyleSheet("font: 12pt \"GOST type A\";\n"
                                     "color: rgb(255, 255, 255);")
        self.lessEqual.setObjectName("lessEqual")
        self.verticalLayout_3.addWidget(self.lessEqual)
        self.moreEqual = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.moreEqual.setStyleSheet("font: 12pt \"GOST type A\";\n"
                                     "color: rgb(255, 255, 255);")
        self.moreEqual.setObjectName("moreEqual")
        self.verticalLayout_3.addWidget(self.moreEqual)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.equation.setText(_translate("MainWindow", "ax² +bx + c = 0"))
        self.discriminant.setText(_translate("MainWindow", "D = b² - 4ac"))
        self.firstAnswer.setText(_translate("MainWindow", "x₁ = b + √D / 2a"))
        self.secondAnswer.setText(_translate("MainWindow", "x₂ = b - √D / 2a"))
        self.quadratic.setText(_translate("MainWindow", "квадратное уравнение"))
        self.biquadratic.setText(_translate("MainWindow", "биквадратное уравнение"))
        self.inequality.setText(_translate("MainWindow", "неравенство"))
        self.secondLab.setText(_translate("MainWindow", "b"))
        self.firstLab.setText(_translate("MainWindow", "a"))
        self.thirdLab.setText(_translate("MainWindow", "c"))
        self.starter.setText(_translate("MainWindow", "Решить"))
        self.uploadBtn.setText(_translate("MainWindow", "Применить"))
        self.less.setText(_translate("MainWindow", "<"))
        self.more.setText(_translate("MainWindow", ">"))
        self.lessEqual.setText(_translate("MainWindow", "≤"))
        self.moreEqual.setText(_translate("MainWindow", "≥"))


class Equation_form(QMainWindow, Ui_MainWindow_equation):
    def __init__(self, **args):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Уравнения/Неравенства')

        self.size = self.secondAnswer.size()

        self.less.hide()
        self.more.hide()
        self.lessEqual.hide()
        self.moreEqual.hide()

        self.firstBox.setMinimum(-99)
        self.secondBox.setMinimum(-99)
        self.thirdBox.setMinimum(-99)

        self.starter.clicked.connect(self.start)
        self.uploadBtn.clicked.connect(self.params)

    def params(self):
        if self.quadratic.isChecked():
            self.secondAnswer.resize(self.size)
            self.less.hide()
            self.more.hide()
            self.lessEqual.hide()
            self.moreEqual.hide()

            self.firstBox.setValue(1)
            self.secondBox.setValue(1)
            self.thirdBox.setValue(1)
            self.equation.setText("ax² + bx + c = 0")

        elif self.biquadratic.isChecked():
            self.secondAnswer.resize(self.size)
            self.less.hide()
            self.more.hide()
            self.lessEqual.hide()
            self.moreEqual.hide()

            self.firstBox.setValue(1)
            self.secondBox.setValue(1)
            self.thirdBox.setValue(1)
            self.equation.setText("ax⁴ + bx² + c = 0")

        elif self.inequality.isChecked():
            self.less.show()
            self.more.show()
            self.lessEqual.show()
            self.moreEqual.show()

            self.firstBox.setValue(1)
            self.secondBox.setValue(1)
            self.thirdBox.setValue(1)

            if self.less.isChecked():
                self.equation.setText("ax² + bx + c < 0")

            elif self.more.isChecked():
                self.equation.setText("ax² + bx + c > 0")

            elif self.lessEqual.isChecked():
                self.equation.setText("ax² + bx + c ≤ 0")

            elif self.moreEqual.isChecked():
                self.equation.setText("ax² + bx + c ≥ 0")

    def start(self):
        a = int(self.firstBox.text())
        b = int(self.secondBox.text())
        c = int(self.thirdBox.text())

        D = (b ** 2) - (4 * a * c)
        self.discriminant.setText(f"D = {D}")

        if self.quadratic.isChecked():
            if D < 0:
                self.firstAnswer.setText("x₁ = ∞")
                self.secondAnswer.setText("x₂ = ∞")

            elif D == 0:
                if a != 0:
                    x = -b / (2 * a)
                if x == 0.0:
                    x = 0
                self.firstAnswer.setText(f"x₁ = {round(x, 2)}")
                self.secondAnswer.setText(f"x₂ = {round(x, 2)}")

            elif D > 0:
                x1 = (-b + sqrt(D)) / (2 * a)
                x2 = (-b - sqrt(D)) / (2 * a)
                self.firstAnswer.setText(f"x₁ = {round(x1, 2)}")
                self.secondAnswer.setText(f"x₂ = {round(x2, 2)}")

        elif self.biquadratic.isChecked():
            if D < 0:
                self.firstAnswer.setText("x₁ = ∞")
                self.secondAnswer.setText("x₂ = ∞")

            elif D == 0:
                t = -b / (2 * a)
                if t == 0.0:
                    self.firstAnswer.setText(f"x₁ = 0")
                    self.secondAnswer.setText(f"x₂ = 0")
                elif t > 0:
                    self.firstAnswer.setText(f"x₁ = ±{round(t ** 0.5, 2)}")
                    self.secondAnswer.setText(f"x₂ = ±{round(t ** 0.5, 2)}")
                else:
                    self.firstAnswer.setText(f"x₁ = нет корней")
                    self.secondAnswer.setText(f"x₂ = нет корней")

            elif D > 0:
                t1 = (-b + sqrt(D)) / (2 * a)
                t2 = (-b - sqrt(D)) / (2 * a)
                if t1 > 0:
                    self.firstAnswer.setText(f"x₁ = ±{round(t1 ** 0.5, 2)}")
                elif t1 == 0:
                    self.firstAnswer.setText(f"x₁ = 0")
                else:
                    self.firstAnswer.setText(f"x₁ = нет корней")

                if t2 > 0:
                    self.secondAnswer.setText(f"x₂ = ±{round(t2 ** 0.5, 2)}")
                elif t2 == 0:
                    self.secondAnswer.setText(f"x₂ = 0")
                else:
                    self.secondAnswer.setText(f"x₂ = нет корней")

        elif self.inequality.isChecked():
            if D < 0:
                self.firstAnswer.setText("x = ∞")
                self.secondAnswer.setText("x ∈ (-∞ ; +∞)")

            elif D == 0:
                x = -b / (2 * a)
                self.firstAnswer.setText(f"x = {round(x, 2)}")

                if self.less.isChecked():
                    if a >= 0:
                        self.secondAnswer.setText(f"x ∈ (-∞ ; {round(x, 2)})")
                    else:
                        self.secondAnswer.setText(f"x ∈ ({round(x, 2)} ; +∞)")

                elif self.more.isChecked():
                    if a >= 0:
                        self.secondAnswer.setText(f"x ∈ ({round(x, 2)} ; +∞)")
                    else:
                        self.secondAnswer.setText(f"x ∈ (-∞ ; {round(x, 2)})")

                elif self.lessEqual.isChecked():
                    if a >= 0:
                        self.secondAnswer.setText(f"x ∈ (-∞ ; {round(x, 2)}]")
                    else:
                        self.secondAnswer.setText(f"x ∈ [{round(x, 2)} ; +∞)")

                elif self.moreEqual.isChecked():
                    if a >= 0:
                        self.secondAnswer.setText(f"x ∈ [{round(x, 2)} ; +∞)")
                    else:
                        self.secondAnswer.setText(f"x ∈ (-∞ ; {round(x, 2)}]")


            elif D > 0:
                x1 = (-b + sqrt(D)) / (2 * a)
                x2 = (-b - sqrt(D)) / (2 * a)
                if x1 > x2:
                    x1, x2 = x2, x1
                self.firstAnswer.setText(f"x₁ = {round(x1, 2)} ; {round(x2, 2)}")

                if self.less.isChecked():
                    if a >= 0:
                        self.secondAnswer.setText(f"x ∈ ({round(x1, 2)} ; {round(x2, 2)})")
                    else:
                        self.secondAnswer.setText(f"x ∈ (-∞ ; {round(x1, 2)}) u ({round(x2, 2)} ; +∞)")
                        self.secondAnswer.adjustSize()

                elif self.more.isChecked():
                    if a >= 0:
                        self.secondAnswer.setText(f"x ∈ (-∞ ; {round(x1, 2)}) u ({round(x2, 2)} ; +∞)")
                        self.secondAnswer.adjustSize()
                    else:
                        self.secondAnswer.setText(f"x ∈ ({round(x1, 2)} ; {round(x2, 2)})")

                elif self.lessEqual.isChecked():
                    if a >= 0:
                        self.secondAnswer.setText(f"x ∈ [{round(x1, 2)} ; {round(x2, 2)}]")
                    else:
                        self.secondAnswer.setText(f"x ∈ (-∞ ; {round(x1, 2)}] u [{round(x2, 2)} ; +∞)")
                        self.secondAnswer.adjustSize()

                elif self.moreEqual.isChecked():
                    if a >= 0:
                        self.secondAnswer.setText(f"x ∈ (-∞ ; {round(x1, 2)}] u [{round(x2, 2)} ; +∞)")
                        self.secondAnswer.adjustSize()
                    else:
                        self.secondAnswer.setText(f"x ∈ [{round(x1, 2)} ; {round(x2, 2)}]")

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_H:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Помощь в уравнениях/неравенствах")
                dlg.setText("""Уравнения:
1)Выберите тип уравнения (не забудьте применить)
2)Укажите коэффиценты
3)Нажмите 'Посчитать'

Неравенства:
1)Укажите знак неравенства (не забудьте применить)
2)Укажите коэффиценты
3)Нажмите 'Посчитать'""")
                dlg.exec()