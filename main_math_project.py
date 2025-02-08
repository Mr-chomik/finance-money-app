import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from equation_window import Equation_form
from currency_window import Currency_form
from graph_window import Graph_form
from calc_window import Calculator_form
from menu_window_ui import Ui_MainWindow_menu


class Menu_form(QMainWindow, Ui_MainWindow_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Меню')
        self.currency.clicked.connect(self.run)
        self.calculator.clicked.connect(self.run)
        self.equation.clicked.connect(self.run)
        self.graph.clicked.connect(self.run)
        self.Menu = self

    def run(self):
        if self.sender().text() == "Валюты":
            self.Currency_form = Currency_form()
            self.Currency_form.show()
            self.showMinimized()

        elif self.sender().text() == "Калькулятор":
            self.Calculator_form = Calculator_form()
            self.Calculator_form.show()
            self.showMinimized()

        elif "Уравнения" in self.sender().text():
            self.Equation_form = Equation_form()
            self.Equation_form.show()
            self.showMinimized()

        elif self.sender().text() == "Графики":
            self.Graph_form = Graph_form()
            self.Graph_form.show()
            self.showMinimized()

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_H:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Помощь в меню")
                dlg.setText("""Выберите желаемую функцию приложения.
                
Если потребуется помощь всегда используйте Ctrl+H""")
                dlg.exec()

    def closeEvent(self, event):
        dialog = QMessageBox.question(self, "Закрытие окна", "Вы действительно хотите закрыть окно?")
        if dialog == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu_form()
    ex.show()
    sys.exit(app.exec())