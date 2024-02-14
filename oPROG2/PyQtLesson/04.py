import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.count = 0

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Четвёртая программа')

        self.btn = QPushButton('0', self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.tick)

    def tick(self):
        self.count += 1
        self.btn.setText(str(self.count))


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
