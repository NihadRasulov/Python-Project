import os
from datetime import date as d


def writeLog(text, *args):
    print(text, args)

    fileName = "text"

    if args:
        try:
            if args[0]:
                print(args[0])
                fileName = args[0]
        except:
            pass

    print(text, fileName)

    print(d.today().strftime("%Y/%m"))
    os.makedirs(d.today().strftime("%Y/%m/%d"), exist_ok=True)

    fileName = d.today().strftime("%Y/%m/%d") + "/" + fileName + ".txt"
    print(fileName)

    file = open(fileName, 'a')
    file.write(text + "\n")
    file.close()


writeLog("hello", "world")
