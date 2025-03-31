# import os
# from datetime import date as d
#
# def writeLog(text, fileName="text"):
#     print(text, fileName)
#
#     folderPath = d.today().strftime("%Y/%m/%d")
#     os.makedirs(folderPath, exist_ok=True)
#
#     filePath = f"{folderPath}/{fileName}.txt"
#     print(filePath)
#
#     with open(filePath, 'a') as file:
#         file.write(text + "\n")
#
# writeLog("hello", "world")

import os
from datetime import date as d

def writeLog(text):

    folder = d.today().strftime("%Y/%m")
    os.makedirs(folder, exist_ok=True)

    file = f"{folder}/{d.today().strftime('%d')}.txt"

    with open(file, 'a+') as file:
        file.write(text + "\n")

writeLog("Hello World")
