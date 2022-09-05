from PyQt5 import QtCore, QtGui, QtWidgets
import RenameWindowImage


class Ui_RenameWindow(object):
    def setupUi(self, RenameWindow):
        RenameWindow.setObjectName("RenameWindow")
        RenameWindow.setFixedSize(600, 400)
        RenameWindow.setStyleSheet("QMainWindow{\n"
                                   "    background-image: url(:/RenameWindowImage/images/Kosa.jpg);\n"
                                   "}")
        RenameWindow.setWindowIcon(QtGui.QIcon(':/RenameWindowImage/images/WindowIcon.ico'))
        self.centralwidget = QtWidgets.QWidget(RenameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NewFileNameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.NewFileNameLine.setGeometry(QtCore.QRect(100, 100, 400, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NewFileNameLine.setFont(font)
        self.NewFileNameLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(255, 0, 0);\n"
                                           "border-style: solid;\n"
                                           "border-width:1px;\n"
                                           "border-radius: 5px;\n"
                                           "border-color: rgb(255, 255, 255);")
        self.NewFileNameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.NewFileNameLine.setObjectName("NewFileNameLine")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 140, 90, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.ORLabel = QtWidgets.QLabel(self.centralwidget)
        self.ORLabel.setGeometry(QtCore.QRect(210, 140, 30, 22))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ORLabel.setFont(font)
        self.ORLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ORLabel.setObjectName("ORLabel")
        self.NewResolutionLine = QtWidgets.QLineEdit(self.centralwidget)
        self.NewResolutionLine.setGeometry(QtCore.QRect(260, 140, 240, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NewResolutionLine.setFont(font)
        self.NewResolutionLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "color: rgb(255, 0, 0);\n"
                                             "border-style: solid;\n"
                                             "border-width:1px;\n"
                                             "border-radius: 5px;\n"
                                             "border-color: rgb(255, 255, 255);")
        self.NewResolutionLine.setAlignment(QtCore.Qt.AlignCenter)
        self.NewResolutionLine.setObjectName("NewResolutionLine")
        self.SelectFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.SelectFolderButton.setGeometry(QtCore.QRect(100, 182, 400, 25))
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
        self.TitleRenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleRenameLabel.setGeometry(QtCore.QRect(50, 10, 441, 91))
        self.TitleRenameLabel.setText("")
        self.TitleRenameLabel.setPixmap(QtGui.QPixmap(":/RenameWindowImage/images/Rename.png"))
        self.TitleRenameLabel.setObjectName("TitleRenameLabel")
        self.InfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.InfoButton.setGeometry(QtCore.QRect(530, 20, 32, 32))
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
        icon.addPixmap(QtGui.QPixmap(":/RenameWindowImage/images/AboutUs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InfoButton.setIcon(icon)
        self.InfoButton.setIconSize(QtCore.QSize(32, 32))
        self.InfoButton.setObjectName("InfoButton")
        RenameWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RenameWindow)
        self.statusbar.setObjectName("statusbar")
        RenameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RenameWindow)
        QtCore.QMetaObject.connectSlotsByName(RenameWindow)

    def retranslateUi(self, RenameWindow):
        _translate = QtCore.QCoreApplication.translate
        RenameWindow.setWindowTitle(_translate("RenameWindow", "Rename"))
        self.NewFileNameLine.setPlaceholderText(
            _translate("RenameWindow", "Enter a new file name, example: BAD_GIRL #"))
        self.comboBox.setItemText(0, _translate("RenameWindow", "mp4"))
        self.comboBox.setItemText(1, _translate("RenameWindow", "jpg"))
        self.ORLabel.setText(_translate("RenameWindow", "or"))
        self.NewResolutionLine.setPlaceholderText(_translate("RenameWindow", "Enter the resolution, example: png"))
        self.SelectFolderButton.setText(_translate("RenameWindow", "Select the desired folder"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    RenameWindow = QtWidgets.QMainWindow()
    ui = Ui_RenameWindow()
    ui.setupUi(RenameWindow)
    RenameWindow.show()
    sys.exit(app.exec_())
