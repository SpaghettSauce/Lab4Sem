import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Первая программа')


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
