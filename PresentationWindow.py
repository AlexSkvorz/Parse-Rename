from PyQt5 import QtCore, QtGui, QtWidgets
import PresentationWindowImage


class Ui_PresentationWindow(object):
    def setupUi(self, PresentationWindow):
        PresentationWindow.setObjectName("PresentationWindow")
        PresentationWindow.setFixedSize(800, 585)
        PresentationWindow.setStyleSheet("QMainWindow{\n"
                                         "    background-image: url(:/PresentationWindowImage/images/Girl.jpg);\n"
                                         "}")
        PresentationWindow.setWindowIcon(QtGui.QIcon(':/PresentationWindowImage/images/WindowIcon.ico'))
        font = QtGui.QFont()
        font.setPointSize(12)
        PresentationWindow.setFont(font)
        PresentationWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(PresentationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RUButton = QtWidgets.QPushButton(self.centralwidget)
        self.RUButton.setGeometry(QtCore.QRect(620, 30, 53, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.RUButton.setFont(font)
        self.RUButton.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);    \n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-radius: 4.2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    max-width:51px;\n"
"    max-height:21px;\n"
"    min-width:51px;\n"
"    min-height:21px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-color: rgb(255,0,0)\n"
"}\n"
"    ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PresentationWindowImage/images/Russia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RUButton.setIcon(icon)
        self.RUButton.setDefault(False)
        self.RUButton.setFlat(False)
        self.RUButton.setObjectName("RUButton")
        self.ENButton = QtWidgets.QPushButton(self.centralwidget)
        self.ENButton.setGeometry(QtCore.QRect(680, 30, 53, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ENButton.setFont(font)
        self.ENButton.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);    \n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-radius: 4.2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    max-width:51px;\n"
"    max-height:21px;\n"
"    min-width:51px;\n"
"    min-height:21px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-color: rgb(255,0,0)\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/PresentationWindowImage/images/England.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ENButton.setIcon(icon1)
        self.ENButton.setObjectName("ENButton")
        self.YTButton = QtWidgets.QPushButton(self.centralwidget)
        self.YTButton.setGeometry(QtCore.QRect(630, 470, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.YTButton.setFont(font)
        self.YTButton.setStyleSheet("QPushButton{\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/PresentationWindowImage/images/Youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.YTButton.setIcon(icon2)
        self.YTButton.setIconSize(QtCore.QSize(30, 30))
        self.YTButton.setObjectName("YTButton")
        self.TGButton = QtWidgets.QPushButton(self.centralwidget)
        self.TGButton.setGeometry(QtCore.QRect(630, 510, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TGButton.setFont(font)
        self.TGButton.setStyleSheet("QPushButton{\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/PresentationWindowImage/images/Telegram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TGButton.setIcon(icon3)
        self.TGButton.setIconSize(QtCore.QSize(32, 32))
        self.TGButton.setObjectName("TGButton")
        self.ParseButton = QtWidgets.QPushButton(self.centralwidget)
        self.ParseButton.setGeometry(QtCore.QRect(200, 400, 400, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ParseButton.setFont(font)
        self.ParseButton.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);    \n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-radius: 4.2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    min-width:51px;\n"
"    min-height:21px;\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-color: rgb(255,0,0)\n"
"}\n"
"    ")
        self.ParseButton.setObjectName("ParseButton")
        self.Rename_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Rename_Button.setGeometry(QtCore.QRect(200, 440, 400, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Rename_Button.setFont(font)
        self.Rename_Button.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);    \n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-radius: 4.2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    min-width:51px;\n"
"    min-height:21px;\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-color: rgb(255,0,0)\n"
"}\n"
"    ")
        self.Rename_Button.setObjectName("Rename_Button")
        self.GitHubButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.GitHubButton_2.setGeometry(QtCore.QRect(630, 430, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.GitHubButton_2.setFont(font)
        self.GitHubButton_2.setStyleSheet("QPushButton{\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/PresentationWindowImage/images/Github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GitHubButton_2.setIcon(icon4)
        self.GitHubButton_2.setIconSize(QtCore.QSize(32, 32))
        self.GitHubButton_2.setObjectName("GitHubButton_2")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(88, 90, 612, 161))
        self.NameLabel.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.NameLabel.setText("")
        self.NameLabel.setPixmap(QtGui.QPixmap(":/PresentationWindowImage/images/Title.png"))
        self.NameLabel.setObjectName("NameLabel")
        self.AuthorLabel = QtWidgets.QLabel(self.centralwidget)
        self.AuthorLabel.setGeometry(QtCore.QRect(280, 220, 441, 81))
        self.AuthorLabel.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.AuthorLabel.setText("")
        self.AuthorLabel.setPixmap(QtGui.QPixmap(":/PresentationWindowImage/images/AlexSkvorz.png"))
        self.AuthorLabel.setObjectName("AuthorLabel")
        PresentationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PresentationWindow)
        self.statusbar.setObjectName("statusbar")
        PresentationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PresentationWindow)
        QtCore.QMetaObject.connectSlotsByName(PresentationWindow)

    def retranslateUi(self, PresentationWindow):
        _translate = QtCore.QCoreApplication.translate
        PresentationWindow.setWindowTitle(_translate("PresentationWindow", "Parse&Rename"))
        self.RUButton.setText(_translate("PresentationWindow", "RU"))
        self.ENButton.setText(_translate("PresentationWindow", "EN"))
        self.YTButton.setText(_translate("PresentationWindow", "Delirious"))
        self.TGButton.setText(_translate("PresentationWindow", "@AlexSkvorz"))
        self.ParseButton.setText(_translate("PresentationWindow", "Parse"))
        self.Rename_Button.setText(_translate("PresentationWindow", "Rename"))
        self.GitHubButton_2.setText(_translate("PresentationWindow", "AlexSkvorz"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PresentationWindow = QtWidgets.QMainWindow()
    ui = Ui_PresentationWindow()
    ui.setupUi(PresentationWindow)
    PresentationWindow.show()
    sys.exit(app.exec_())