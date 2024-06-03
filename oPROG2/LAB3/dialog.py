from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class DialogForm(QDialog):
    def __init__(self):
        
        super().__init__()
        uic.loadUi("DialogWindow.ui", self)
