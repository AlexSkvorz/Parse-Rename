import json
import sys
import webbrowser
import subprocess

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore
from natsort import os_sorted

import ParseWindow
import PresentationWindow
import RenameWindow

import openpyxl
import os


class Presentation(QtWidgets.QMainWindow, PresentationWindow.Ui_PresentationWindow):
    def __init__(self):
        super(Presentation, self).__init__()
        self.Parse = Parse()
        self.Rename = Rename()
        self.setupUi(self)

        self.ParseButton.clicked.connect(self.open_parse)
        self.Rename_Button.clicked.connect(self.open_rename)
        self.RUButton.clicked.connect(self.translate_ru)
        self.ENButton.clicked.connect(self.translate_en)

        self.GitHubButton_2.clicked.connect(lambda: webbrowser.open('https://github.com/AlexSkvorz'))
        self.YTButton.clicked.connect(
            lambda: webbrowser.open('https://www.youtube.com/channel/UCfO5AL_kNukBt-Dk0TjcQfw'))
        self.TGButton.clicked.connect(lambda: webbrowser.open('https://t.me/AlexSkvorz'))

    def open_parse(self):
        self.Parse.show()

    def open_rename(self):
        self.Rename.show()

    def translate_ru(self):
        self.ParseButton.setText('Парсинг')
        self.Rename_Button.setText('Переименование')
        self.Parse.translate_ru()
        self.Rename.translate_ru()

    def translate_en(self):
        self.ParseButton.setText('Parse')
        self.Rename_Button.setText('Rename')
        self.Parse.translate_en()
        self.Rename.translate_en()


class Parse(QtWidgets.QMainWindow, ParseWindow.Ui_ParseWindow):
    def __init__(self):
        super(Parse, self).__init__()
        self.setupUi(self)

        self.AddButton.clicked.connect(self.add_item)
        self.DeleteButton.clicked.connect(self.del_item)
        self.ClearButton.clicked.connect(self.clear_all)
        self.SelectFolderButton.clicked.connect(self.parsing)
        self.ru = False

    def add_item(self):
        item = self.CentralLine.text()
        self.CentralList.addItem(item)
        self.CentralLine.setText('')

    def del_item(self):
        clicked = self.CentralList.currentRow()
        self.CentralList.takeItem(clicked)

    def clear_all(self):
        self.CentralList.clear()

    def translate_ru(self):
        self.AddButton.setText('Добавить имя')
        self.DeleteButton.setText('Удалить имя')
        self.ClearButton.setText('Очистить все')
        self.SelectFolderButton.setText('Выбрать нужную папку')
        self.CentralLine.setPlaceholderText('Введите имена столбцов, которые будут в файле Excel')
        self.XLSLine.setPlaceholderText('Введите имя Excel файла, например: BAD_GIRLS')
        self.ru = True

    def translate_en(self):
        self.AddButton.setText('Add a column')
        self.DeleteButton.setText('Delete a column')
        self.ClearButton.setText('Clear all')
        self.SelectFolderButton.setText('Select the desired folder')
        self.CentralLine.setPlaceholderText('Enter the names of the columns that will be in Excel file')
        self.XLSLine.setPlaceholderText('Enter the name that Excel file will have, example: BAD_GIRLS')

    def parsing(self):
        if self.CentralList.count() != 0:
            book = openpyxl.Workbook()
            sheet = book.active
            for i in range(self.CentralList.count()):
                sheet[chr(65 + i) + '1'] = f'{self.CentralList.item(i).text()}'

            try:
                directory = QFileDialog.getExistingDirectory()
                files = os.listdir(directory)
                files = os_sorted(files)
                ext = 'json'
                row = 2
                flag = False
                for filename in files:
                    if filename.endswith(ext):
                        flag = True
                        with open(directory + '/' + filename) as jsfile:
                            data = json.load(jsfile)
                            sheet[row][0].value = data['name']
                            string = 0
                        for atr in data['attributes']:
                            string += 1
                            sheet[row][string].value = atr['value']
                        row += 1

                if not flag:
                    if self.ru:
                        QMessageBox.critical(self, "Ошибка", "Нет подходящих файлов", QMessageBox.Ok)
                    else:
                        QMessageBox.critical(self, "Error", "No matching files", QMessageBox.Ok)
                else:
                    if self.XLSLine.text() == '':
                        if self.ru:
                            QMessageBox.critical(self, "Ошибка", "Введите имя Excel файла", QMessageBox.Ok)
                        else:
                            QMessageBox.critical(self, "Error", "Enter Excel file name", QMessageBox.Ok)
                    else:
                        output = subprocess.check_output(r'powershell -command "[Environment]::'
                                                         r'GetFolderPath(\"Desktop\")"')
                        path = output.decode().strip()
                        book.save(f'{path}/{self.XLSLine.text()}.{"xlsx"}')

                        if self.ru:
                            QMessageBox.information(self, "Успешно", "Файл " + f'{self.XLSLine.text()}.{"xlsx"}'
                                                    + " успешно сохранён на рабочем столе")
                        else:
                            QMessageBox.information(self, "Complete", "File " + f'{self.XLSLine.text()}.{"xlsx"}'
                                                    + " has been successfully saved on the desktop")
            except WindowsError:
                if self.ru:
                    QMessageBox.critical(self, "Ошибка", "Выберите папку", QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error", "Choose any folder", QMessageBox.Ok)
            except IndexError:
                if self.ru:
                    QMessageBox.critical(self, "Ошибка", "Добавьте корректное число атрибутов", QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error", "Enter the correct number of attributes", QMessageBox.Ok)
        else:
            if self.ru:
                QMessageBox.critical(self, "Ошибка", "Добавьте имена колонок", QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Error", "Add column names", QMessageBox.Ok)

    def keyPressEvent(self, e):
        if e.key() in [QtCore.Qt.Key_Return]:
            self.add_item()
        elif e.key() in [QtCore.Qt.Key_Backspace]:
            self.del_item()


class Rename(QtWidgets.QMainWindow, RenameWindow.Ui_RenameWindow):
    def __init__(self):
        super(Rename, self).__init__()
        self.setupUi(self)

        self.SelectFolderButton.clicked.connect(self.renaming)
        self.ru = False
        self.flagName = False

    def translate_ru(self):
        self.NewFileNameLine.setPlaceholderText('Введите новое имя файла, например: BAD_GIRL #')
        self.NewResolutionLine.setPlaceholderText('Введите разрешение, прим.: png')
        self.ORLabel.setText('или')
        self.ORLabel.setGeometry(200, 140, 55, 22)
        self.SelectFolderButton.setText('Выбрать нужную папку')
        self.ru = True

    def translate_en(self):
        self.NewFileNameLine.setPlaceholderText('Enter a new file name, example: BAD_GIRL #')
        self.NewResolutionLine.setPlaceholderText('Enter the resolution, example: png')
        self.ORLabel.setText('or')
        self.ORLabel.setGeometry(210, 140, 30, 22)
        self.SelectFolderButton.setText('Select the desired folder')

    def renaming(self):
        if self.NewFileNameLine.text() or self.flagName:
            self.ext = self.comboBox.currentText()
            try:
                directory = QFileDialog.getExistingDirectory()
                files = os.listdir(directory)
                files = os_sorted(files)
                i = 1

                if self.NewResolutionLine.text():
                    self.ext = self.NewResolutionLine.text()

                for filename in files:
                    if filename.endswith(self.ext):
                        name = self.NewFileNameLine.text() + str(i)
                        os.rename(f'{directory}/{filename}', f'{directory}/{name}.{self.ext}')
                        i = i + 1
                if i == 1:
                    if self.ru:
                        QMessageBox.critical(self, "Ошибка",
                                             "Файлов с разрешением ." + self.ext + " в выбранной папке нет",
                                             QMessageBox.Ok)
                    else:
                        QMessageBox.critical(self, "Error", "Files with permission ." + self.ext +
                                             "  is not in the selected folder", QMessageBox.Ok)
                else:
                    if self.ru:
                        QMessageBox.information(self, "Успешно", str(i - 1) + ' файла(ов) успешно переименованы')
                    else:
                        QMessageBox.information(self, "Complete", str(i - 1) + ' files successfully renamed')
            except WindowsError:
                if self.ru:
                    QMessageBox.critical(self, "Ошибка", "Выберите папку", QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Error", "Choose any folder", QMessageBox.Ok)
        else:
            self.flagName = True
            if self.ru:
                QMessageBox.warning(self, "Внимание", "Введите новое имя для файлов, "
                                                      "иначе они будут просто пронумерованы")
            else:
                QMessageBox.warning(self, "Attention", "Enter a new name for the files, "
                                                       "otherwise they will just be numbered ")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Presentation()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
