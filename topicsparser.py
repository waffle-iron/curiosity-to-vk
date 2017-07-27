# -*- coding: utf-8 -*-
import logging
import requests
import re
import json
from bs4 import BeautifulSoup
import trendingparser
from trendingparser import TrendingParser
import dis
import inspect
import pyrebase
from io import open as iopen
import grab
from grab import Grab
from PIL import Image, ImageFont, ImageDraw, ImageEnhance


class Curiosity:

    #регулярные выражения
    re_zero_img = re.compile(r"https://curiosity-data\.s3\.amazonaws\.com/images/content/meme/standard/(.*?)\.png")

    #списки с английским тектом
    topic_title = []
    topic_img_1_href = []
    topic_img_1_scr = []
    topic_img_0_href = []
    topic_img_0_hrefs = []
    topic_img_0_scr =[]
    topic_channel = []
    topic_text_1 = []

    #списки с русским текстом
    topic_channel_ru = []
    topic_text_1_ru = []
    topic_title_ru = []


    def __init__(self, a):
        self.a = a


    @staticmethod
    #работа с базой данных
    def database():
        config = {
            "apiKey": "AIzaSyD6EzxDobegHGvkorLEle6OBt_RNedkD0g",
            "authDomain": "project-3931781304531690229.firebaseapp.com",
            "databaseURL": "https://project-3931781304531690229.firebaseio.com",
            "projectId": "project-3931781304531690229",
            "storageBucket": "project-3931781304531690229.appspot.com",
            "type": "service_account",
            "project_id": "project-3931781304531690229",
            "private_key_id": "fa36c163c3267295a17d6c34a7bbfb9fbb7fb860",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDH+ULfO0USH5/e\n8W274zuSjKMySBIJxU14tB1C+Sl4QREeMbndzflcnJ+HnRDNyvDL5Y9iaiHC+5Ao\nqdPJigr4ggR/jXZ7BMsAEcVVqyzzFZmnqhAdX//uxzjJQZFe8EdANdArhUHMWNr5\nWqY3zG27IqpxRb/75UevY3rWhiWiaIjSyCprNOhs1n16FG1Tjlgi1tG9C8F335qK\nAYiW1FhEZKYqDe82AZSTWwqx/hVl4D+m4BRpmvwbVdJY6cNqWKYUn7HcptmdpSon\nNLX5YxB02ATj1N9jjxzYxaw+msL0oN9ad1/2uzwl1CwdBVRpRGVl3gw6qAxgkTiR\ntExt33T5AgMBAAECggEBAJHiE5jKok7gZz67HfSNhu4YTw3ladNa7nN54kbzgf9K\naHSAjjlzg9C+KdtDB/k5bYUxyPJgvpSB9N7VVb2XSP2VzDZJOv/vtTAtxqoCoF4N\nifS4qdzkJc9J4vFfNe/ulewP1feJ1UCAKe7y5IOcTQjR90l/OtlGoI8goYJShq39\nDoEvp7oSQ3yy3WXSj+WwFrLPz79eLpFymw3WdJ1PRi2y2/ls+wLe5ostEG+FD3kq\ndGDOXXB+FJPJuJrODf6m9qPlxTQkWEXhMYMpMgfKWiAOKhNYYJQ4IpJLSXu4H3WY\ncVPaGRE1df9lrq1yBS35aWzeortebhWrlNKLHSUS4gECgYEA5D28n3NtSNYYhJhO\nLbvXvt7k80RyB+n/bZnX3U42NFrLdMt2yrB59MuDKkgKZubBZMBAZu6FDo6wC/6r\nSRbB30a3KoNlXhLeOGNGRqYLrJBL76Oxt0Ekm68nRdQEGbUUKza5hNoKJLnwBzdD\nazgUBc2gdncfw0xYdrKZ8QNhwpkCgYEA4EtrYk6b3ll2hVaWyZEYXA7upz+24A4k\neafLKMNP3tr0HU9V6VVcZRK72mRrAeBGAoSDm5/Mgvk8XQwr52/zvuV8yim1wmGd\nR1mpYGGSWBFaMxPwSgaBIOhDG0a3HSzfoTGXbUig0WaquMXXOrLk1b8HSBHPMWwR\n5Dm5LJAXIWECgYBS1ZkkYXbzLUh+ruwIqxjU2/5Jz7h26NTcCS6P0ffYLm+Sttkp\nHL1WO5oh+T1VNUBQ+XkmIkDGFMENyWKOxySbjQWi90cNylk+K8FwmIi6GzCEC2vP\nL2RC4GGndRf74H0uZdEUxzFRPO5BICxmuFaD+KnY9MjhT0733UADeY+8WQKBgQDG\nEnRTTV4ifljHKY9hk6uyaFFjC0YhGPwnHwGvDsPy5uLbG1ugAgzlCSUxmKpS7s6E\nnKdogDbnltgyx3PiHyBefWS1Vx42+WMeRlToU2IcOb6xCrORe6r+932DkfBVaHJY\ndGXoUVILeiHbqIMISEEDbX4tq+SQHYKzTDJ14w06IQKBgDZFDIVgk4v81yH0M+oe\nJ1oDUpFj//wVWfuOjalR/+udBIIVJXILchm6rVHOnTEWmvxFZCcD7Zxhy5pEGSDg\nHM/pHOPth8vh5qquEH+Ji613bp/VXVysN37xkpa23fhxSgankqbFiJoxpqOhgWYe\nxgKAzkt34Fug8XYO+hDAbL3X\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-alb7j@project-3931781304531690229.iam.gserviceaccount.com",
            "client_id": "105042264485843483839",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-alb7j%40project-3931781304531690229.iam.gserviceaccount.com",
            "serviceAccount": "/home/ubuntu/workspace/curiosity-to-vk/pycache/kirsanov-dot-com-fa36c163c326.json"
            }

        firebase = pyrebase.initialize_app(config)

        # Получить ссылку на службу авторизации
        auth = firebase.auth()

        uid = 'some-uid'

        custom_token = auth.create_custom_token(uid)

        # Зарегистрировать пользователя в базе
        user = auth.sign_in_with_email_and_password("danilakirsanovspb@gmail.com", "Nhb1,e2yfk3$")

        # Получить ссылку на службу базы данных
        db = firebase.database()

        data = {
            "curiosity/topics/"+ str(href).replace('http://curiosity.com/topics/', ''): {
                'id': db.generate_key(),
                'title': title,
                'description': text_1,
                'channel': channel,
                'img': img_1[0]
            }
        }

        db.update(data)

        #Передайте idToken пользователя методу push
        #results = db.child("curiosity").child("topics").push(data, user['idToken'])


    @staticmethod
    #парсинг информации из топиков
    def topicsparser():

        in_db, new, to_post = TrendingParser.change_href()

        for href in new:

            r = requests.get(href)

            html = r.text

            soup = BeautifulSoup(html, "lxml")

            topic_page = soup.find("div", {"class": "topic-page"})

            head = topic_page.find_all("div", {"class": "image-header"})

            body = topic_page.find_all("div", {"class": "content-item"})

            regexp_img_1 = re.compile(r'/curiosity-data\.s3\.amazonaws\.com/images/content/hero/standard/(.*?)\.png\"\)')

            for item in head:

                img_1 = re.findall(regexp_img_1, item.find('style').text)

                text_1 = body[0].find("p").text

                if item.find("div", {"class": "header-content"}).find('a') != None:

                    channel = item.find("div", {"class": "header-content"}).find('a').text

                    title = item.find("div", {"class": "header-content"}).find('h1').text

                elif item.find("div", {"class": "header-content"}).find('a') == None:

                    channel = item.find("div", {"class": "header-content"}).find('h5').text

                    title = item.find("div", {"class": "header-content"}).find('h1').text

            #заполняем список каналов
            Curiosity.topic_channel.append(str(channel))

            #заполняем список заголовков
            Curiosity.topic_title.append(str(title))

            #заполняем список ссылок на изображения
            Curiosity.topic_img_1_href.append("http://curiosity-data.s3.amazonaws.com/images/content/hero/standard/" + img_1[0] + ".png")

            #заполняем список первых текстов
            Curiosity.topic_text_1.append(str(text_1))


    @staticmethod
    #скачиваем изображения обложек постов
    def img_0_downloader():
        respon = requests.get("http://curiosity.com/trending/")
        html = respon.text
        zero_img_srcs = re.findall(Curiosity.re_zero_img, html)
        for x in zero_img_srcs[::3]:
            Curiosity.topic_img_0_hrefs.append(x)
        count = 0
        max_ind = len(Curiosity.topic_img_0_hrefs) - 1
        while count <= max_ind:
            Curiosity.topic_img_0_href.append("http://curiosity-data.s3.amazonaws.com/images/content/meme/standard/"+Curiosity.topic_img_0_hrefs[count]+".png")
            res = requests.get(Curiosity.topic_img_0_href[count])
            with open('/home/ubuntu/workspace/curiosity-to-vk/topics/zero-img-'+str(count)+'.png', 'wb') as zero:
                zero.write(res.content)
            Curiosity.topic_img_0_scr.append('/home/ubuntu/workspac/curiosity-to-v/topics/zero-img-'+str(count)+'.png')
            count = count + 1


    @staticmethod
    #скачиваем изображения, заполняем список адресов к картинкам в нашей фс
    def img_1_downloader():

        #Скачивает главные изображения постов
        g_first_img = Grab(timeout=20)
        g_first_img.setup(headers={'chrome-proxy': 's=Ci4KEwjMhrTr79_TAhXQIBkKHQH0A0USDAib-sXIBRCojrrZAxoJCgdkZWZhdWx0EkgwRgIhAIdAgOu3URu5cs-VjgT5MlOXD8ckBB3udUqTMeXYIGc0AiEAmdK5TxX33uuUGLrtjrZGzKNXOnV4NIJg6YKU50BVMsA=, c=win, b=3029, p=96'})
        count = 0
        max_index = len(Curiosity.topic_img_1_href) - 1
        while count <= max_index:
            resp = g_first_img.go(Curiosity.topic_img_1_href[count])
            open('/home/ubuntu/workspace/curiosity-to-vk/topics/'+str(count)+'.png', 'wb').write(resp.body)
            #заполняем список адресов к картинкам для нашей фс
            Curiosity.topic_img_1_scr.append('/home/ubuntu/workspace/curiosity-to-vk/topics/'+str(count)+'.png')
            count = count + 1

        return Curiosity.topic_img_1_scr


    @staticmethod
    #перевод статьи curiosity на руский язык
    def translater():
        #временные переменные для циклов
        count = 0
        max_index = len(Curiosity.topic_channel) - 1

        #переводим списки
        while count <= max_index:
            #канал
            channel = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_channel[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            #заголовок
            title = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_title[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            #параграф № 1
            text_1 = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_text_1[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }

            # делаем запрос к яндекс переводчику и сохраняем ответ
            channel_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=channel).json()
                #канал
            title_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=title).json()
                #заголовок
            text_1_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=text_1).json()
                #параграф 1

            #заполняем списки с русским текстом
            Curiosity.topic_title_ru.append(title_ru['text'])
                #заголовок
            Curiosity.topic_channel_ru.append(channel_ru['text'])
                #канал
            Curiosity.topic_text_1_ru.append(text_1_ru['text'])
                #параграф 1

            #условие итерации
            count = count + 1

        return Curiosity.topic_channel_ru, Curiosity.topic_title_ru, Curiosity.topic_text_1_ru


    @staticmethod
    def painter(count):

        # Название канала
        channel = Curiosity.topic_channel_ru[count][0].upper()

        # Заголовок
        title = Curiosity.topic_title_ru[count][0]

        # изображение для модификации
        img_composit = Image.open("./topics/zero-img-"+str(count)+".png").convert("RGBA")

        # прозрачный загрузчик логотипов
        logo_painter = Image.open('./logo-playload.png').convert("RGBA")

        # кисть для загрузчика
        logo_painter_draw = ImageDraw.Draw(logo_painter)

        # шрифты
        channel_font = ImageFont.truetype("./topics/Roboto-Fosts/Roboto-Bold.ttf", 24)

        # размер блока текста с названием канала в списке
        channel_size = channel_font.getsize(channel)

        # размер блока текста с названием канала в кортеже
        _size = (channel_size[0] + 20, channel_size[1] + 20)

        # пустые изображение для нанесения текста с названием канала
        channel_im = Image.open('./Button.png').convert("RGBA")

        # изменяем размер изображения
        channel_img = channel_im.resize(_size, resample=0)

        # кисть для пустое изображение для нанесения текста с названием канала
        channel_draw = ImageDraw.Draw(channel_img)

        # процедура нанесения мультистрокового текста с названием канала на изобрание
        x = (_size[0] - channel_size[0]) / 2
        y = (_size[1] - channel_size[1]) / 2
        channel_draw.multiline_text((x, y), channel, font=channel_font, align="center")

        # наносим заголовок на загрузцик
        logo_painter_draw.multiline_text((10, 945), title, font=channel_font, align="left")

        # наносим канал и заголовок на загрузчик
        logo_painter.paste(channel_img, (5, 900))

        # композиция обложки и загрузчика логотипов
        composition = Image.alpha_composite(img_composit, logo_painter)

        # процедура сохранения композиционной обложки в файл
        composition.save("./topics/zero-img-"+str(count)+"-composite.png")  # compositeon.save("./topics/zero-img-0    -composit.png")


#======ТЕСТЫ==========ТЕСТЫ===============ТЕСТЫ=============ТЕСТЫ==============


    @staticmethod
    def test():
        Curiosity.topicsparser()
        Curiosity.translater()
        Curiosity.img_0_downloader()
        Curiosity.img_1_downloader()
        print(Curiosity.topic_channel_ru, Curiosity.topic_title_ru, Curiosity.topic_text_1_ru)
        count = 0
        max_index = 9
        while count <= max_index:
            Curiosity.painter(count)
            count = count + 1
Curiosity.test()
if __name__ == "__main__":
    print("Любопытcтво делает вас умнее")