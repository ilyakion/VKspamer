# -*- coding: utf-8 -*-
try:
    import vk_api
except:
    import pip
    pip.main(["install", "vk_api"])
    import vk_api

from Function import *
import random
import threading

class main:
    def __init__(self):
        reserv("Программа запущена")
        print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))
        group=["", "exclusive_muzic", "kino_kaif", "vkmuz", "kino_mania", "ifun", "record"]
#        group = ["liandil_team"]

        akks = []

        proces = []

        try:

        except:
            print("error Авторизии")

        try:
            print("Введите время посева:")
            timeW = int(input())
            print("Введите время перед стартом:")
            wait = int(input())

            time.sleep(wait*60)

            NomberAkk = random.randint(0, (len(akks)-1))

            for i in akks:
                proces.append(threading.Thread(target=i.SmartComentNew, args=(akks[NomberAkk], ("Плейлист любителя","Топовый плейлист","Музыка из Tik Tok","Цель-10000 прослушиваний","🔥Плейлист любителя🔥"), "audio_playlist345817947_17_10db7b92855f6d3834", timeW)))
#                proces.append(threading.Thread(target=i.comentNew, args=(akks, "🔥Плейлист любителя🔥", "audio_playlist345817947_17_10db7b92855f6d3834", timeW)))
#                i.coment("liandil_team", "Плейлист любителя", 0, "audio_playlist345817947_17_10db7b92855f6d3834")

                if NomberAkk >= len(akks) - 1:
                    NomberAkk = 0
                else:
                    NomberAkk += 1

            for i in proces:
                i.start()
                time.sleep(random.randint(0, 100)/10)
        except:
            print("error main")
        reserv("конец работы")

main()