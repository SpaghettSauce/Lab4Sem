# Form implementation generated from reading ui file 'c:\Users\Spaghet\Desktop\PROGVS\GIIT\Lab4Sem\oPROG2\LAB2\designer.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1008, 528)
        self.city_label = QtWidgets.QLabel(parent=Form)
        self.city_label.setGeometry(QtCore.QRect(60, 30, 161, 33))
        self.city_label.setObjectName("city_label")
        self.btn = QtWidgets.QPushButton(parent=Form)
        self.btn.setGeometry(QtCore.QRect(800, 30, 71, 31))
        self.btn.setObjectName("btn")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 30, 561, 31))
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 130, 361, 391))
        self.listWidget.setStyleSheet("border-color: rgb(255, 170, 0);")
        self.listWidget.setObjectName("listWidget")
        self.address_label = QtWidgets.QLabel(parent=Form)
        self.address_label.setGeometry(QtCore.QRect(440, 130, 55, 16))
        self.address_label.setText("")
        self.address_label.setObjectName("address_label")
        self.time_label = QtWidgets.QLabel(parent=Form)
        self.time_label.setGeometry(QtCore.QRect(440, 200, 55, 16))
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(680, 130, 291, 391))
        self.textEdit.setStyleSheet("border-color: rgb(255, 3, 3);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        self.lineEdit.returnPressed.connect(self.btn.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.city_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Введите город:</span></p></body></html>"))
        self.btn.setText(_translate("Form", "OK"))
