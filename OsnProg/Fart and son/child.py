from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox

class Child(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Child_Design.ui",self)
        self.okButton.clicked.connect(self.okPressed)
    def okPressed(self):
        if self.nameEdit.text().isalpha():
            self.accept()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Название лол")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()