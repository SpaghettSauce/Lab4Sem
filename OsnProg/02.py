import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая программа')

        # Лучше добавить btn как атрибут в self
        btn = QPushButton('Кнопка', self)
        btn.resize(100, 100)
        btn.move(100, 100)


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
