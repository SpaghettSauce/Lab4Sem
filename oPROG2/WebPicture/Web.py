from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QImage, QPixmap

import requests

class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("FormDesigner.ui",self)
        self.pushButton.clicked.connect(self.press)
    def press(self):
        api_server = "http://static-maps.yandex.ru/1.x/"

        lon = 37.530887
        lat = 55.703118
        delta = 5.0

        my_params = {
            "ll": f"{lon},{lat}",
            "spn": f"{delta},{delta}",
            "l": "map"
        }

        response = requests.get(api_server, params=my_params)

        if response:
            image = QImage()
            image.loadFromData(response.content)
            p = QPixmap(image)
            self.label.setPixmap(p)
        else:
            print("Что-то пошло не так.")
            print("Код ответа:", response.status_code)
            print("Причина:", response.reason)



app = QApplication([])
wnd = Form()
wnd.show()
app.exec()
