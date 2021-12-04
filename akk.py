# -*- coding: utf-8 -*-
try:
    import vk_api
except:
    import pip

    pip.main(["install", "vk_api"])
    import vk_api

from Function import *
import time
import random

class akk:
    def __init__(self, nomber1, password):

        global nomber
        nomber = '/' + str(nomber1) + '\ '

        vk_session = vk_api.VkApi(str(nomber1), str(password))
        vk_session.auth()

        self.vk = vk_session.get_api()
        reserv("Аккаунт " + str(nomber) + "запущен")

    def post(self, massage='', attachments='0'):
        if str(attachments)!='0':
            if massage!='':
                self.vk.wall.post(message=massag, attachments=str(attachments))
            else:
                self.vk.wall.post(attachments=str(attachments))
            reserv(massage + " (вложение): " + str(attachments))
        else:
            self.vk.wall.post(message=massage)
            reserv(massage)

    def send(self, ip, massage):
        self.vk.messages.send(user_id=str(ip), message=massage, random_id=0)
        reserv(nomber + '-->' + str(id) + '|' + massage)

    def coment(self, ip, massage='', nomb=0, attachments='0'):
        postidlist = self.vk.wall.get(domain=str(ip), count=1, offset=nomb)
        data = str(postidlist["items"][0]['date'])
        postid = str(postidlist["items"][0]["id"])
        ownerid = str(postidlist["items"][0]["from_id"])
        try:
            if str(attachments) != '0':
                if massage != '':
                    self.vk.wall.createComment(owner_id=ownerid, message=massage, post_id=postid, attachments=str(attachments))
                else:
                    self.vk.wall.createComment(owner_id=ownerid, post_id=postid, attachments=str(attachments))
                reserv(ip + '|размещено:' + data + '|' + massage + " (вложение): " + str(attachments))
            else:
                self.vk.wall.createComment(owner_id=ownerid, message=massage, post_id=postid)
                reserv(ip + '|размещено:' + data + '|' + massage)
        except:
            reserv("!Ошибка коментирования! " + ip + '|размещено:' + data + '|' + massage + " (вложение): " + str(attachments))

    def comentNew(self, ip, massage, attachments='0', timeW=5):
        #time в минуты
        timeS = time.time()
        posts = []
        reserv("запущен посев в группу: " + str(ip) + " на " + str(timeW) + " минут |" + str(massage) + " (вложение): " + str(attachments))
        while time.time()-timeS < timeW*60:
            postidlist = self.vk.wall.get(domain=str(ip), count=1, offset=0)
            postid0 = str(postidlist["items"][0]["id"])
            postidlist = self.vk.wall.get(domain=str(ip), count=1, offset=1)
            postid1 = str(postidlist["items"][0]["id"])
            if not postid0 in posts:
                akk.coment(self, ip, massage, 0, attachments)
                posts.append(postid0)
            time.sleep(1)
            if not postid1 in posts:
                akk.coment(self, ip, massage, 1, attachments)
                posts.append(postid1)
            time.sleep(30)
        reserv("посев окончен: " + str(ip) + " на " + str(timeW) + " минут |" + str(massage) + " (вложение): " + str(attachments) + " (" + time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()) + ")")


    def SmartComentNew(self, ip, massage, attachments='0', timeW=5):
        #time в минуты
        timeS = time.time()
        postidlist = self.vk.wall.get(domain=str(ip), count=1, offset=0)
        print(postidlist)
        StartPostID0 = str(postidlist["items"][0]["id"])
        postidlist = self.vk.wall.get(domain=str(ip), count=1, offset=1)
        StartPostID1 = str(postidlist["items"][0]["id"])
        posts = [StartPostID0, StartPostID1]
        reserv("запущен Smart посев в группу: " + str(ip) + " на " + str(timeW) + " минут |" + str(massage) + " (вложение): " + str(attachments))
        NombMassage = random.randint(0, (len(massage)-1))
        while time.time()-timeS < timeW*60:
            postidlist = self.vk.wall.get(domain=str(ip), count=1, offset=0)
            postid0 = str(postidlist["items"][0]["id"])
            postidlist = self.vk.wall.get(domain=str(ip), count=1, offset=1)
            postid1 = str(postidlist["items"][0]["id"])

            if not postid0 in posts:
                akk.coment(self, ip, massage[NombMassage], 0, attachments)
                posts.append(postid0)
            time.sleep(1)
            if not postid1 in posts:
                akk.coment(self, ip, massage[NombMassage], 1, attachments)
                posts.append(postid1)

            if NombMassage >= len(massage)-1:
                NombMassage = 0
            else:
                NombMassage += 1

            time.sleep(10)
        reserv("Smart посев окончен: " + str(ip) + " на " + str(timeW) + " минут |" + str(massage) + " (вложение): " + str(attachments) + " (" + time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()) + ")")