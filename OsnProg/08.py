from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.children = []

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Главная форма')

        self.btn = QPushButton('Открыть другую форму', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 100)

        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        #self.second_form = SecondForm(self, "Текст для второй формы")
        new_form = SecondForm(self, "Текст для второй формы")
        self.children.append(new_form)
        #self.second_form.show()
        new_form.show()

    def closeEvent(self, event):
        #for x in self.chidlren:
            #x.close()
        event.ignore()

class SecondForm(QWidget):
    def __init__(self, parent, caption):
        super().__init__()

        self.setGeometry(400, 400, 300, 300)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(caption, self)
        self.lbl.adjustSize()

# pyinstaller --onefile 08.py --windowed --icon=flower.ico
app = QApplication([])
ex = FirstForm()
ex.show()
app.exec()
