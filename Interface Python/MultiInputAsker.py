# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiInputAsker.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(747, 537)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 450, 271, 36))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 30, 631, 371))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Multi Input through .csv"))
        self.pushButton.setText(_translate("Form", "Yes, It has the required columns"))
        self.label.setText(_translate("Form", "Make sure, your csv file has the following heading as the columns headings:\n"
"\n"
"variety name\n"
"system of cultivation\n"
"is irrigated\n"
"yielding type\n"
"pest damage\n"
"seeds per hectare\n"
"operation size\n"
"cultivation size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

