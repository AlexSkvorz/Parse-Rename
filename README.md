# **Parse & Rename**

:rocket: The **application** is designed **for parsing information from JSON files in EXCEL**, as well as **for renaming a large volume of files of the same type.** 

**The application is made using PyQt5.**
___
## **Installation**
To launch the application, you need to perform a simple action - run the file Parse-Rename.exe.

## **Exploitation**
The program has two main functions.
![](https://github.com/AlexSkvorz/Parse-Rename/blob/master/Screens-For-README/First.png)

### **The first is the parsing of JSON files**

To work correctly, we need to enter the column names, which should be equal to the name and all attributes. After that, add the name of the folder and select the path where our JSON lies. An example (on 10 JSON) can be seen in the screenshots.

![](https://github.com/AlexSkvorz/Parse-Rename/blob/master/Screens-For-README/Second.png)

![](https://github.com/AlexSkvorz/Parse-Rename/blob/master/Screens-For-README/Third.png)

![](https://github.com/AlexSkvorz/Parse-Rename/blob/master/Screens-For-README/Fourth.png)

![](https://github.com/AlexSkvorz/Parse-Rename/blob/master/Screens-For-README/Fifth.png)

The program processes all JSON files located in this folder. In case of correct operation, an EXCEL file with the name you entered will appear on the desktop. Otherwise, the program will tell you what might be wrong.

:bangbang: **Attention** :bangbang:

JSON files must have the same structure to work correctly.

### **The second is renaming files**

This function of the application is convenient for renaming a large number of files of the same resolution. 

To work, you must specify the desired name for the file, the ones following it will have the same name, but with a different serial number. The resolution can be selected in the ComboBox, or specified manually. Then just select the folder with the files.

![](https://github.com/AlexSkvorz/Parse-Rename/blob/master/Screens-For-README/Sixth.png)

![](https://github.com/AlexSkvorz/Parse-Rename/blob/master/Screens-For-README/Seventh.png)

![](https://github.com/AlexSkvorz/Parse-Rename/blob/master/Screens-For-README/Eigth.png)

:bangbang: **Attention** :bangbang:

Files after renaming will be sorted in the same order as in Windows
 
## **Built with**

+ Python 3.10
+ Qt Designer
+ PyQt5

## **Author**
+ Telegram - [AlexSkvorz](https://t.me/AlexSkvorz)
+ VK - [AlexSkvorz](https://vk.com/alexskvorz)
