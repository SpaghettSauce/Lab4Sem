import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Седьмая программа. Кто отправил сигнал?')

        self.button_1 = QPushButton(self)
        self.button_1.move(90, 40)
        self.button_1.setText("Кнопка 1")
        self.button_1.clicked.connect(self.run)

        self.button_2 = QPushButton(self)
        self.button_2.move(90, 80)
        self.button_2.setText("Кнопка 2")
        self.button_2.clicked.connect(self.run)

        self.label = QLabel(self)
        self.label.setText("Пока никто не отправлял")
        self.label.move(50, 120)

    def run(self):
        self.label.setText(self.sender().text())
        print(self.sender().text())


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
