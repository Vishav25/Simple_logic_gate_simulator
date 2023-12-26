# Logic Gate Simulator

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 90, 181, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(530, 90, 181, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 280, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.NOR = QtWidgets.QPushButton(self.centralwidget) #NOR button
        self.NOR.setGeometry(QtCore.QRect(340, 400, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NOR.setFont(font)
        self.NOR.setObjectName("NOR")
        self.NAND = QtWidgets.QPushButton(self.centralwidget) #Nand BUTTON
        self.NAND.setGeometry(QtCore.QRect(162, 397, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NAND.setFont(font)
        self.NAND.setObjectName("NAND")
        self.XOR = QtWidgets.QPushButton(self.centralwidget) #XOR button
        self.XOR.setGeometry(QtCore.QRect(520, 400, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.XOR.setFont(font)
        self.XOR.setObjectName("XOR")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.NOR.clicked.connect(self.norClicked)
        self.NAND.clicked.connect(self.nandClicked)
        self.XOR.clicked.connect(self.xorClicked)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.comboBox.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "Result ="))
        self.NOR.setText(_translate("MainWindow", "NOR"))
        self.NAND.setText(_translate("MainWindow", "NAND"))
        self.XOR.setText(_translate("MainWindow", "XOR"))

    def nandClicked(self):
        firstValue = int(self.comboBox.currentText())
        secondValue = int(self.comboBox_2.currentText())
        nand = not(firstValue and secondValue)
        if nand == True:
            nand = 1
        else:
            nand = 0
        self.label.setText(str(firstValue) + " NAND " + str(secondValue) + " = " + str(nand))

    def norClicked(self):
        firstValue = int(self.comboBox.currentText())
        secondValue = int(self.comboBox_2.currentText())
        nor = not(firstValue or secondValue)
        if nor == True:
            nor = 1
        else:
            nor = 0
        self.label.setText(str(firstValue) + " NOR " + str(secondValue) + " = " + str(nor))

    def xorClicked(self):
        firstValue = int(self.comboBox.currentText())
        secondValue = int(self.comboBox_2.currentText())
        xor = (firstValue and not secondValue) or (not firstValue and secondValue)
        if xor == True:
            xor = 1
        else:
            xor = 0
        self.label.setText(str(firstValue) + " XOR " + str(secondValue) + " = " + str(xor))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
