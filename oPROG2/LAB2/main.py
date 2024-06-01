from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QListWidgetItem

from sys import exit as sys_exit
import requests


class Belarus(QWidget):
    def __init__(self):
        request_string = "https://belarusbank.by/api/kursExchange"
        response = requests.get(request_string)
        if not response:
            print("О оу.")
            print("Код ответа:", response.status_code)
            print("Причина:", response.reason)
            sys_exit(1)

        super().__init__()
        self.setFixedSize(1008, 561)

        uic.loadUi("designer.ui", self)
        self.response_json = response.json()
        self.btn.clicked.connect(self.button)
        self.listWidget.itemClicked.connect(self.itemcl)

    def button(self):
        if self.listWidget.count() > 0:
            self.listWidget.clear()
        user_input = self.lineEdit.text().strip().lower()    
        for el in self.response_json:
            if user_input == el["name"].strip().lower():
                self.listWidget.addItem(QListWidgetItem(el["filials_text"]))

    def itemcl(self, item):
        for el in self.response_json:
            if item.text() == el["filials_text"]:
                self.address_label.setText(f"<b>Адрес:</b> {el['street_type']} {el['street']}, {el['home_number']}")
                self.address_label.adjustSize()
                time_list = []
                for time in el['info_worktime'].split("|")[:-1]:
                    if time[-5].isdigit():
                        
                        if len(time) > 18:
                            time_list.append(
                                f"{time[:2]}: {time[3:5]}:{time[6:8]} - {time[9:11]}:{time[12:14]} (пер. {time[15:17]}:{time[18:20]} - {time[21:23]}:{time[24:26]})")
                        else:
                            time_list.append(f"{time[:2]}: {time[3:5]}:{time[6:8]} - {time[9:11]}:{time[12:14]}")


                time_list = "<br/>".join(time_list)
                self.time_label.setText(f"<b>Время работы</b><br/>{time_list}")
                self.time_label.adjustSize()


                self.textEdit.clear()
                self.textEdit.setReadOnly(True)  # setDisabled
                currency_list = ["USD", "EUR", "RUB", "GBP", "CAD", "PLN", "SEK", "CHF", "JPY", "CNY", "CZK", "NOK"]
                for currency in currency_list:
                    self.textEdit.append(
                        f"<b>{currency}</b><br/>Покупка: {el[f'{currency}_in']}<br/>Продажа: {el[f'{currency}_out']}<br/><br/>")


app = QApplication([])
wnd = Belarus()
wnd.show()
app.exec()
