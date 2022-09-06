# **Parse & Rename**
The **application** is designed **for parsing information from JSON files in EXCEL**, as well as **for renaming a large volume of files of the same type.** 

**The application is made using PyQt5.**
___
## **Installation**
To launch the application, you need to perform a simple action - run the file Parse-Rename.exe.

## **Exploitation**
The program has two main functions.
![](https://downloader.disk.yandex.ru/preview/5d6e86d08ef9cd7c37257ce478d9234b154c377fd1bf9847360045992ab07327/6317ab23/iogmq--JR47TS_-gmJO3GPTWE8qDY4lyfoyvM90ZZi3SveR1UewySwjGqkdbuztVcy9HV-KMs8i0AbOzKzPcdQ%3D%3D?uid=0&filename=First.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

### **The first is the parsing of JSON files**

To work correctly, we need to enter the column names, which should be equal to the name and all attributes. After that, add the name of the folder and select the path where our JSON lies. An example (on 10 JSON) can be seen in the screenshots.

![](https://downloader.disk.yandex.ru/preview/3a28f322c8d81984a22ea4a77bd9b6b330f95e50a6f684ebc0f249ace0c27e7b/6317ab36/8cU86-rLJ9KJ626iB4KlkOcPS6p1U8eiuyg4fDaBT6o5B-fnokxwjENLSStfbgkERbTBFnS7loFBEWLqQAw3Ng%3D%3D?uid=0&filename=Second.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![](https://downloader.disk.yandex.ru/preview/bec217e49575998adce88d0ba1ccd81d3d9e6e973fad1528398cfe2c159078e4/6317ab47/7Qcf9M39I8pIUJmaoAF5Qjyqmms_-ZSxkAzBDtMsxu4by0-z2aHk7q6q3KOH-2EReoXVsIP8nqNKcWkrPzzjBg%3D%3D?uid=0&filename=Third.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![](https://downloader.disk.yandex.ru/preview/951a04eeac895afc7d9e8d2a74eda03c00eea5cd002edacba853bb5124a40e41/6317ab59/aFsDnpMREnosLPUFUqgAVheHfwAPfWTevSFITIrex9OcQiyOU5LrKtqf88ZBg2Q_97gaNdzCWG7l1g5UjHb6OA%3D%3D?uid=0&filename=Fourth.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![](https://3.downloader.disk.yandex.ru/preview/968dffcf823540122e475fece63b57483a1fe3fbe0d1dc4bb7d388e1c7788090/inf/kTLrsXUG6LmdYDQFhsQsCyy4ldl7MEfsyayOhQNzpTdFuGBt_JoBL99W2VPeK8mTo9zr_OR9-ZTUDBNh87WFZA%3D%3D?uid=1514580312&filename=Fifth.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1514580312&tknv=v2&size=958x1003)

The program processes all JSON files located in this folder. In case of correct operation, an EXCEL file with the name you entered will appear on the desktop. Otherwise, the program will tell you what might be wrong.

:bangbang:Attention!!!

JSON files must have the same structure to work correctly.

### **The second is renaming files**

This function of the application is convenient for renaming a large number of files of the same resolution. 

To work, you must specify the desired name for the file, the ones following it will have the same name, but with a different serial number. The resolution can be selected in the ComboBox, or specified manually. Then just select the folder with the files.

![](https://2.downloader.disk.yandex.ru/preview/eb5fd731e9ecee2b574420ef9be08b62a479845f42f573b9f5bc04d4513dadde/inf/Fx1SLPJU-DySYPV6fEOyewzgVEtISVJfrXYHAzzksfZfbhmkpTcKoluuwF3G25ma5jsGt-iHeamUcirmN02sBA%3D%3D?uid=1514580312&filename=Sixth.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1514580312&tknv=v2&size=958x1003)

![](https://4.downloader.disk.yandex.ru/preview/191cccf2160062fd364ccd9fea201f280a24187cb6875a652d0a2035fb97f54b/inf/7Qcf9M39I8pIUJmaoAF5Qjyqmms_-ZSxkAzBDtMsxu4by0-z2aHk7q6q3KOH-2EReoXVsIP8nqNKcWkrPzzjBg%3D%3D?uid=1514580312&filename=Third.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1514580312&tknv=v2&size=958x1003)

![](https://4.downloader.disk.yandex.ru/preview/a14ea00dd08d3036df219b7d03f73a25c7213cc265839aa16b151d225860fa2d/inf/bJQgMEY7kD2PBMnJgPsaIgzgVEtISVJfrXYHAzzksfYYSyu2y3bC7UhP_DC2EbqOJYy8UnnCQ2mkaIVeBN7rXQ%3D%3D?uid=1514580312&filename=Eigth.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1514580312&tknv=v2&size=958x1003)

:bangbang:Attention!!!

Files after renaming will be sorted in the same order as in Windows
 
## **Built with**

+ Python 3.10
+ Qt Designer
+ PyQt5

## **Author**
+ Telegram - [AlexSkvorz](https://t.me/AlexSkvorz)
+ VK - [AlexSkvorz](https://vk.com/alexskvorz)