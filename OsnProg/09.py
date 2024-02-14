from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import io

class MyExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
        self.pushButton.clicked.connect(self.press)

    def press(self):
        s = self.nameEdit.text()
        self.helloLabel.setText(f"Hello, <b>{self.lineEdit.text()}</b>!")


if hasattr(PyQt5.Qtcore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(PyQt5.QtCore.Qt.AA_Enable)
if hasattr(PyQt5.Qtcore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(PyQt5.QtCore.Qt.AA_Enable)

app = QApplication([])
ex = MyExample()
ex.show()
app.exec()
