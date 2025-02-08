import sys


from pyqtgraph import PlotWidget
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox


class Ui_MainWindow_graph(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 530)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, 711, 311))
        self.graphicsView.setStyleSheet("border-color: rgb(232, 232, 232);\n"
                                        "background-color: rgb(117, 117, 117);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(760, 40, 151, 89))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.line.setStyleSheet("font: 15pt \"GOST type A\";\n"
                                "color: rgb(255, 255, 255);")
        self.line.setChecked(True)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.parabola = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.parabola.setStyleSheet("font: 15pt \"GOST type A\";\n"
                                    "color: rgb(255, 255, 255);")
        self.parabola.setChecked(False)
        self.parabola.setObjectName("parabola")
        self.verticalLayout.addWidget(self.parabola)
        self.hyperbola = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.hyperbola.setStyleSheet("font: 15pt \"GOST type A\";\n"
                                     "color: rgb(255, 255, 255);")
        self.hyperbola.setObjectName("hyperbola")
        self.verticalLayout.addWidget(self.hyperbola)
        self.func_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.func_label.setGeometry(QtCore.QRect(30, 360, 161, 31))
        self.func_label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(235, 235, 235);")
        self.func_label.setObjectName("func_label")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 400, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.firstBox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.firstBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.firstBox.setObjectName("firstBox")
        self.gridLayout.addWidget(self.firstBox, 0, 1, 1, 1)
        self.secondBox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.secondBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.secondBox.setObjectName("secondBox")
        self.gridLayout.addWidget(self.secondBox, 1, 1, 1, 1)
        self.thirdLab = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.thirdLab.setStyleSheet("color: rgb(255, 255, 255);")
        self.thirdLab.setObjectName("thirdLab")
        self.gridLayout.addWidget(self.thirdLab, 2, 0, 1, 1)
        self.secondLab = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.secondLab.setStyleSheet("color: rgb(255, 255, 255);")
        self.secondLab.setObjectName("secondLab")
        self.gridLayout.addWidget(self.secondLab, 1, 0, 1, 1)
        self.firstLab = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.firstLab.setStyleSheet("color: rgb(255, 255, 255);")
        self.firstLab.setObjectName("firstLab")
        self.gridLayout.addWidget(self.firstLab, 0, 0, 1, 1)
        self.thirdBox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.thirdBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.thirdBox.setObjectName("thirdBox")
        self.gridLayout.addWidget(self.thirdBox, 2, 1, 1, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(760, 160, 151, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.XcheckBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        self.XcheckBox.setStyleSheet("font: 14pt \"GOST Type AU\";\n"
                                     "color: rgb(255, 255, 255);")
        self.XcheckBox.setObjectName("XcheckBox")
        self.verticalLayout_3.addWidget(self.XcheckBox)
        self.YcheckBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        self.YcheckBox.setStyleSheet("font: 14pt \"GOST Type AU\";\n"
                                     "color: rgb(255, 255, 255);")
        self.YcheckBox.setObjectName("YcheckBox")
        self.verticalLayout_3.addWidget(self.YcheckBox)
        self.drawer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.drawer.setGeometry(QtCore.QRect(577, 360, 161, 53))
        self.drawer.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "font: 25 20pt \"Segoe UI Light\";")
        self.drawer.setObjectName("drawer")
        self.uploadBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.uploadBtn.setGeometry(QtCore.QRect(780, 240, 111, 31))
        self.uploadBtn.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "font: 14pt \"Times New Roman\";")
        self.uploadBtn.setObjectName("uploadBtn")
        self.verticalLayoutWidget.raise_()
        self.graphicsView.raise_()
        self.func_label.raise_()
        self.gridLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.drawer.raise_()
        self.uploadBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 21))
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
        self.line.setText(_translate("MainWindow", "Прямая"))
        self.parabola.setText(_translate("MainWindow", "Парабола"))
        self.hyperbola.setText(_translate("MainWindow", "Гипербола"))
        self.func_label.setText(_translate("MainWindow", "y = kx + b"))
        self.thirdLab.setText(_translate("MainWindow", "b"))
        self.secondLab.setText(_translate("MainWindow", "Степень X"))
        self.firstLab.setText(_translate("MainWindow", "k"))
        self.XcheckBox.setText(_translate("MainWindow", "Сетка X"))
        self.YcheckBox.setText(_translate("MainWindow", "Сетка Y"))
        self.drawer.setText(_translate("MainWindow", "Построить"))
        self.uploadBtn.setText(_translate("MainWindow", "Применить"))


class Graph_form(QMainWindow, Ui_MainWindow_graph):
    def __init__(self, **args):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Графики')
        self.drawer.clicked.connect(self.draw)
        self.uploadBtn.clicked.connect(self.params)

    def params(self):
        if self.line.isChecked():
            self.firstBox.setValue(1)
            self.secondBox.setValue(1)
            self.thirdBox.setValue(0)

            self.firstBox.setMinimum(-199)
            self.secondBox.setMinimum(0)
            self.thirdBox.setMinimum(-199)

            self.func_label.setText("y = kx + b")
            self.firstLab.setText("k")
            self.secondLab.setText("Степень X")
            self.thirdLab.setText("b")

        elif self.parabola.isChecked():
            self.firstBox.setValue(1)
            self.secondBox.setValue(1)
            self.thirdBox.setValue(0)

            self.firstBox.setMinimum(-199)
            self.secondBox.setMinimum(-199)
            self.thirdBox.setMinimum(-199)

            self.func_label.setText("y = ax² + bx + c")
            self.firstLab.setText("a")
            self.secondLab.setText("b")
            self.thirdLab.setText("c")

        elif self.hyperbola.isChecked():
            self.firstBox.setValue(1)
            self.secondBox.setValue(1)
            self.thirdBox.setValue(1)

            self.firstBox.setMinimum(-199)
            self.secondBox.setMinimum(0)
            self.thirdBox.setMinimum(1)

            self.func_label.setText("y = a / kx")
            self.firstLab.setText("a")
            self.secondLab.setText("Степень X")
            self.thirdLab.setText("k")

        if self.XcheckBox.isChecked():
            self.graphicsView.showGrid(y=True)
        else:
            self.graphicsView.showGrid(y=False)

        if self.YcheckBox.isChecked():
            self.graphicsView.showGrid(x=True)
        else:
            self.graphicsView.showGrid(x=False)

    def draw(self):
        if self.line.isChecked():
            koef = int(self.firstBox.text())
            step = int(self.secondBox.text())
            other = int(self.thirdBox.text())
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-100, 101)],
                                   [((i ** step) * koef) + other for i in range(-100, 101)], pen='b')

        elif self.parabola.isChecked():
            a = int(self.firstBox.text())
            b = int(self.secondBox.text())
            c = int(self.thirdBox.text())
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(-100, 101)],
                                   [(i ** 2 * a) + (b * i) + c for i in range(-100, 101)], pen='b')

        elif self.hyperbola.isChecked():
            a = int(self.firstBox.text())
            step = int(self.secondBox.text())
            k = int(self.thirdBox.text())

            x = [[i for i in range(-100, 0)], [i for i in range(1, 101)]]
            y = [[a / (k * i ** step) for i in range(-100, 0)], [a / (k * i ** step) for i in range(1, 101)]]
            self.graphicsView.clear()
            for i in range(2):
                self.graphicsView.plot(x[i], y[i], pen='b')

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_H:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Помощь в графиках")
                dlg.setText("""Для построения графика:
1)Выберите тип графика (не забудьте применить)
2)Выберите прочие настройки (не забудьте применить)
3)Укажите коэффиценты
4)Нажмите 'Построить'""")
                dlg.exec()