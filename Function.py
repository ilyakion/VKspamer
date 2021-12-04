# -*- coding: utf-8 -*-
import time

def reserv(send):
    print(send)
    file = open("history.txt", 'a')
    STime = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    try:
        file.write(str(STime) + " --- " + str(send) + "\n")
    except:
        send = str(send)
        file.write(str(STime) + " --- ")
        for i in send:
            try:
                file.write(i)
            except:
                file.write("#")
        file.write("\n")
    file.close()