from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QDialog
from child import Child

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Father(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Father_Design.ui",self)
        self.nameButton.clicked.connect(self.press)
    def press(self):
        sonny = Child()
        result = sonny.exec()
        if result == QDialog.Accepted:
            s = sonny.nameEdit.text()
            self.helloLabel.setText(f"Приветт, <b>{s}</b>!")

app = QApplication([])
daddy = Father()
daddy.show()
app.exec()





