from PyQt5 import QtCore, QtGui, QtWidgets
import ParseWindowImage


class Ui_ParseWindow(object):
    def setupUi(self, ParseWindow):
        ParseWindow.setObjectName("ParseWindow")
        ParseWindow.setFixedSize(600, 800)
        ParseWindow.setStyleSheet("QMainWindow{\n"
                                  "    background-image: url(:/ParseWindowImage/images/Black.jpg);\n"
                                  "}")
        ParseWindow.setWindowIcon(QtGui.QIcon(':/ParseWindowImage/images/WindowIcon.ico'))
        self.centralwidget = QtWidgets.QWidget(ParseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.InfoButton.setGeometry(QtCore.QRect(540, 20, 32, 32))
        self.InfoButton.setStyleSheet("QPushButton{\n"
                                      "    background-color: rgb(255, 0, 0, 0);    \n"
                                      "    max-width:51px;\n"
                                      "    max-height:32px;\n"
                                      "    min-width:16px;\n"
                                      "    min-height:16px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    border-style: solid;\n"
                                      "    border-width:1px;\n"
                                      "    border-radius: 4.2px;\n"
                                      "    border-color: rgb(255, 0, 0)\n"
                                      "}")
        self.InfoButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ParseWindowImage/images/AboutUs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InfoButton.setIcon(icon)
        self.InfoButton.setIconSize(QtCore.QSize(32, 32))
        self.InfoButton.setObjectName("InfoButton")
        self.CentralLine = QtWidgets.QLineEdit(self.centralwidget)
        self.CentralLine.setGeometry(QtCore.QRect(100, 140, 400, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CentralLine.setFont(font)
        self.CentralLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(255, 0, 0);\n"
                                       "border-style: solid;\n"
                                       "border-width:1px;\n"
                                       "border-radius: 5px;\n"
                                       "border-color: rgb(255, 255, 255);")
        self.CentralLine.setAlignment(QtCore.Qt.AlignCenter)
        self.CentralLine.setObjectName("CentralLine")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(100, 180, 120, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("QPushButton{\n"
                                     "    color: rgb(255, 255, 255);    \n"
                                     "    border-style: solid;\n"
                                     "    border-width:1px;\n"
                                     "    border-radius: 4.2px;\n"
                                     "    border-color: rgb(255, 255, 255);\n"
                                     "    min-width:51px;\n"
                                     "    min-height:21px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    border-color: rgb(255,0,0)\n"
                                     "}\n"
                                     "    ")
        self.AddButton.setObjectName("AddButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(240, 180, 120, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet("QPushButton{\n"
                                        "    color: rgb(255, 255, 255);    \n"
                                        "    border-style: solid;\n"
                                        "    border-width:1px;\n"
                                        "    border-radius: 4.2px;\n"
                                        "    border-color: rgb(255, 255, 255);\n"
                                        "    min-width:51px;\n"
                                        "    min-height:21px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    border-color: rgb(255,0,0)\n"
                                        "}\n"
                                        "    ")
        self.DeleteButton.setObjectName("DeleteButton")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(380, 180, 120, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClearButton.setFont(font)
        self.ClearButton.setStyleSheet("QPushButton{\n"
                                       "    color: rgb(255, 255, 255);    \n"
                                       "    border-style: solid;\n"
                                       "    border-width:1px;\n"
                                       "    border-radius: 4.2px;\n"
                                       "    border-color: rgb(255, 255, 255);\n"
                                       "    min-width:51px;\n"
                                       "    min-height:21px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "    border-color: rgb(255,0,0)\n"
                                       "}\n"
                                       "    ")
        self.ClearButton.setObjectName("ClearButton")
        self.CentralList = QtWidgets.QListWidget(self.centralwidget)
        self.CentralList.setGeometry(QtCore.QRect(100, 230, 400, 400))
        self.CentralList.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(255,0,0);\n"
                                       "border-style: solid;\n"
                                       "border-width:1px;\n"
                                       "border-radius: 5px;\n"
                                       "")
        self.CentralList.setObjectName("CentralList")
        item = QtWidgets.QListWidgetItem()
        self.CentralList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.CentralList.addItem(item)
        self.SelectFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.SelectFolderButton.setGeometry(QtCore.QRect(100, 700, 400, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SelectFolderButton.setFont(font)
        self.SelectFolderButton.setStyleSheet("QPushButton{\n"
                                              "    color: rgb(255, 255, 255);    \n"
                                              "    border-style: solid;\n"
                                              "    border-width:1px;\n"
                                              "    border-radius: 4.2px;\n"
                                              "    border-color: rgb(255, 255, 255);\n"
                                              "    min-width:51px;\n"
                                              "    min-height:21px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    border-color: rgb(255,0,0)\n"
                                              "}")
        self.SelectFolderButton.setObjectName("SelectFolderButton")
        self.XLSLine = QtWidgets.QLineEdit(self.centralwidget)
        self.XLSLine.setGeometry(QtCore.QRect(100, 655, 400, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.XLSLine.setFont(font)
        self.XLSLine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.XLSLine.setAutoFillBackground(False)
        self.XLSLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "color: rgb(255, 0, 0);\n"
                                   "border-style: solid;\n"
                                   "border-width:1px;\n"
                                   "border-radius: 5px;\n"
                                   "border-color: rgb(255, 255, 255);")
        self.XLSLine.setAlignment(QtCore.Qt.AlignCenter)
        self.XLSLine.setObjectName("XLSLine")
        self.TitleParseLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleParseLabel.setGeometry(QtCore.QRect(0, 5, 381, 131))
        self.TitleParseLabel.setText("")
        self.TitleParseLabel.setPixmap(QtGui.QPixmap(":/ParseWindowImage/images/Parse.png"))
        self.TitleParseLabel.setObjectName("TitleParseLabel")
        ParseWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ParseWindow)
        self.statusbar.setObjectName("statusbar")
        ParseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ParseWindow)
        QtCore.QMetaObject.connectSlotsByName(ParseWindow)

    def retranslateUi(self, ParseWindow):
        _translate = QtCore.QCoreApplication.translate
        ParseWindow.setWindowTitle(_translate("ParseWindow", "Parse"))
        self.CentralLine.setPlaceholderText(
            _translate("ParseWindow", "Enter the names of the columns that will be in Excel file"))
        self.AddButton.setText(_translate("ParseWindow", "Add a column"))
        self.DeleteButton.setText(_translate("ParseWindow", "Delete a column"))
        self.ClearButton.setText(_translate("ParseWindow", "Clear all"))
        __sortingEnabled = self.CentralList.isSortingEnabled()
        self.CentralList.setSortingEnabled(False)
        item = self.CentralList.item(0)
        item.setText(_translate("ParseWindow", "sdadsa"))
        item = self.CentralList.item(1)
        item.setText(_translate("ParseWindow", "dsad"))
        self.CentralList.setSortingEnabled(__sortingEnabled)
        self.SelectFolderButton.setText(_translate("ParseWindow", "Select the desired folder"))
        self.XLSLine.setPlaceholderText(
            _translate("ParseWindow", "Enter the name that Excel file will have, example: BAD_GIRLS"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ParseWindow = QtWidgets.QMainWindow()
    ui = Ui_ParseWindow()
    ui.setupUi(ParseWindow)
    ParseWindow.show()
    sys.exit(app.exec_())
