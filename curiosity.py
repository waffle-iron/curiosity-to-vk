# -*- coding: utf-8 -*-
import requests
import re
import CuriosityTrendingparser
import pyrebase
from PIL import Image, ImageFont, ImageDraw
import CuriosityTopicparser
from bs4 import BeautifulSoup
from grab import Grab


class Curiosity:
    # регулярные выражения
    re_zero_img = re.compile(r"https://curiosity-data\.s3\.amazonaws\.com/images/content/meme/standard/(.*?)\.png")
    # списки с английским тектом
    topic_href = []
    topic_channel = []
    topic_title = []
    topic_img_0_href = []
    topic_img_0_hrefs = []
    topic_img_0_scr = []
    topic_img_0_alt = []
    topic_text_1 = []
    topic_img_1_href = []
    topic_img_1_scr = []
    topic_paragraph_2_title = []
    topic_paragraph_2_text = []
    topic_img_2_href = []
    topic_img_2_src = []
    topic_paragraph_3_title = []
    topic_paragraph_3_text = []
    topic_img_3_href = []
    topic_img_3_src = []
    topic_video_1_title = []
    topic_video_1_data_scr = []
    # списки с русским текстом
    topic_channel_ru = []
    topic_title_ru = []
    topic_img_0_alt_ru = []
    topic_text_1_ru = []
    topic_paragraph_2_title_ru = []
    topic_paragraph_2_text_ru = []
    topic_paragraph_3_title_ru = []
    topic_paragraph_3_text_ru = []

    def __init__(self, *args):
        self.args = args

    @staticmethod
    # БРИГАДИР работ с базой данных
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

        # инициализация базы

        firebase = pyrebase.initialize_app(config)

        # Получить ссылку на службу авторизации
        auth = firebase.auth()  # uid = 'some-uid'; custom_token = auth.create_custom_token(uid)

        # Зарегистрировать пользователя в базе
        user = auth.sign_in_with_email_and_password("danilakirsanovspb@gmail.com", "Nhb1,e2yfk3$")

        # Получить ссылку на службу базы данных
        db = firebase.database()

        data = {
            "curiosity/topics/" + str(Curiosity.topic_href).replace('http://curiosity.com/topics/', ''): {
                'id': db.generate_key(),
                'channel': Curiosity.topic_channel_ru,
                'title': Curiosity.topic_title_ru,
                'description': Curiosity.topic_text_1_ru,
                'img': Curiosity.topic_img_1_scr[0]
            }

        }

        db.update(data)

        # Передайте idToken пользователя методу push
        # results = db.child("curiosity").child("topics").push(data, user['idToken'])

    @staticmethod
    # АНАЛИЗАТОР информации из топиков
    def topicsparser():

        # СЛОВАРЬ ВОЗВРАЩАЕМЫЙ В РЕЗУЛЬТАТЕ АНАЛИЗА

        parse_result = {
            "href": None,
            "channel": None,
            "title": None,
            "img_0_href": None,
            "img_0_scr": None,
            "img_1_href": None,
            "img_1_scr": None,
            "text_1": None,
            "paragraph_2_title": None,
            "paragraph_2_text": None,
            "img_3_href": None,
            "img_3_scr": None,
            "paragraph_3_title": None,
            "paragraph_3_text": None,
            "video_1_title": None,
            "video_1_data_src": None
        }

        # реализация анализатора трендов
        href_in_db, href_new, href_to_post = CuriosityTrendingparser.TrendingParser.change_href()

        # НАЧАЛО ЦИКЛА ОБХОДА МАССИВА ССЫЛОК
        count = 0
        max_index = len(href_new) - 1
        while count <= max_index:
            img_1_href, channel, title, text_1, img_2_href, paragraph_2_title, paragraph_2_text, img_3_href, paragraph_3_title, paragraph_3_text, video_1_title, video_1_data_scr = CuriosityTopicparser.topic_parser(
                    href_new[count])

                # ЗАПОЛНЯЕМ СПИСКИ В СЛОВАРЕ
                # каналы

            Curiosity.topic_channel.append(str(channel))

                # заголовки
            Curiosity.topic_title.append(str(title))

                # ссылок на 1 изображения
            Curiosity.topic_img_1_href.append(
                    "http://curiosity-data.s3.amazonaws.com/images/content/hero/standard/" + img_1_href[0] + ".png")

                # текты первых блоков
            Curiosity.topic_text_1.append(str(text_1))

                # ссылки на 2 изображения
            Curiosity.topic_img_2_href.append(str(img_2_href))

                # заголовки вторых параграфов
            Curiosity.topic_paragraph_2_title.append(str(paragraph_2_title))

                # тексты 2-х параграфов
            Curiosity.topic_paragraph_2_text.append(str(paragraph_2_text))

                # ссылки на 3 изображения
            Curiosity.topic_img_3_href.append(str(img_3_href))

                # заголовки третьих параграфов
            Curiosity.topic_paragraph_3_title.append(str(paragraph_3_title))

                # тексты 3-их параграфов
            Curiosity.topic_paragraph_3_text.append(str(paragraph_3_text))

                # заголовки видеороликов
            Curiosity.topic_video_1_title.append(str(video_1_title))

                # ссылки на видеоролики
            Curiosity.topic_video_1_data_scr.append(str(video_1_data_scr))
            count = count + 1

    @staticmethod
    # АНАЛИЗАТОР заманухи на обложку поста
    def img_0_alt_parser():
        respon = requests.get("http://curiosity.com/trending/day/")
        html = respon.text
        soup = BeautifulSoup(html, "lxml")
        trending_grid = soup.find("div", {"class": "js-trending-grid"})
        all_a = trending_grid.find_all("a")
        alts = []
        for item in all_a:
            alts.append(str(item["title"]))
        return alts

    @staticmethod
    # ПЕРЕВОДЧИК
    def translater():

        # временные переменные для циклов
        count = 0
        max_index = len(Curiosity.topic_channel) - 1

        # переводим списки
        while count <= max_index:

            # канал
            channel = {
                "key": "trnsl.1.1.20170730T114755Z.994753b77b648f24.f3ed7d2f59fcb232c089a1a3328c0e0b900d4925",
                "text": f"{Curiosity.topic_channel[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            # заголовок
            title = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_title[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            # замануха
            alt = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_img_0_alt[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            # параграф № 1
            text_1 = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_text_1[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            # параграф 2 заголовок
            paragraph_2_title = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_paragraph_2_title[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            # параграф 2 текст
            paragraph_2_text = {
                "key": "trnsl.1.1.20170730T114755Z.994753b77b648f24.f3ed7d2f59fcb232c089a1a3328c0e0b900d4925",
                "text": f"{Curiosity.topic_paragraph_2_text[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            # параграф 3 заголовок
            paragraph_3_title = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_paragraph_3_title[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }
            # параграф 2 заголовок
            paragraph_3_text = {
                "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
                "text": f"{Curiosity.topic_paragraph_3_text[count]}.",
                'lang': 'en-ru',
                'format': 'plain'
            }

            # делаем запрос к яндекс переводчику и сохраняем ответ
            channel_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=channel).json()
            # канал
            title_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=title).json()
            # заголовок
            text_1_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=text_1).json()

            paragraph_2_title_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=paragraph_2_title).json()

            paragraph_2_text_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=paragraph_2_text).json()

            paragraph_3_title_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=paragraph_3_title).json()

            paragraph_3_text_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=paragraph_3_text).json()

            img_0_alt_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=alt).json()

            # заполняем списки с русским текстом

            Curiosity.topic_title_ru.append(title_ru['text'][0])
            # заголовок
            Curiosity.topic_channel_ru.append(channel_ru['text'][0])
            # канал
            Curiosity.topic_text_1_ru.append(text_1_ru['text'][0])

            Curiosity.topic_paragraph_2_title_ru.append(paragraph_2_title_ru['text'][0])

            Curiosity.topic_paragraph_2_text_ru.append(paragraph_2_text_ru['text'][0])

            Curiosity.topic_paragraph_3_title_ru.append(paragraph_3_title_ru['text'][0])

            Curiosity.topic_paragraph_3_text_ru.append(paragraph_3_text_ru['text'][0])

            Curiosity.topic_img_0_alt_ru.append(img_0_alt_ru["text"][0])

            # условие итерации
            count = count + 1

    @staticmethod
    # КИСТЬ
    def draw(count):

        # Название канала
        channel = Curiosity.topic_channel_ru[count].upper()

        # Заголовок
        title = Curiosity.topic_title_ru[count]

        # замануха

        alt = Curiosity.topic_img_0_alt_ru[count]

        # изображение для модификации
        img_composit = Image.open("./topics/zero-img-" + str(count) + ".png").convert("RGBA")

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
        logo_painter_draw.multiline_text((10, 975), title, font=channel_font, align="left")
        logo_painter_draw.multiline_text((10, 945), alt, font=channel_font, align="left")
        # наносим канал и заголовок на загрузчик
        logo_painter.paste(channel_img, (5, 900))

        # композиция обложки и загрузчика логотипов
        composition = Image.alpha_composite(img_composit, logo_painter)

        # процедура сохранения композиционной обложки в файл
        composition.save("./topics/zero-img-" + str(
            count) + "-composite.png")  # compositeon.save("./topics/zero-img-0    -composit.png")

    @staticmethod
    # ХУДОЖНИК
    def painters():
        # ЦИКЛ ПРОХОДА ИЗОБРАЖЕНИЙ ДЛЯ ХУДОЖНИКА
        count = 0
        max_index = len(Curiosity.topic_title) - 1
        while count <= max_index:
            Curiosity.draw(count)
            count = count + 1
        return print(f"ХУДОЖНИК УСПЕШНО ОТРИСОВАЛ {max_index} ИЗОБРАЖЕНИЙ")

    @staticmethod
    # скачиваем изображения обложек постов
    def img_0_downloader():
        # TODO поставить колпиляцию restring в цикл и уменьшить паттерн до минимума, тогда. смотреть img_0.py
        respon = requests.get("http://curiosity.com/trending/day/")
        html = respon.text
        zero_img_srcs = re.findall(Curiosity.re_zero_img, html)
        for x in zero_img_srcs[::3]:
            Curiosity.topic_img_0_hrefs.append(x)
        count = 0
        max_ind = len(Curiosity.topic_channel) - 1
        while count <= max_ind:
            Curiosity.topic_img_0_href.append(
                "http://curiosity-data.s3.amazonaws.com/images/content/meme/standard/" + Curiosity.topic_img_0_hrefs[
                    count] + ".png")
            res = requests.get(Curiosity.topic_img_0_href[count])
            with open('./topics/zero-img-' + str(count) + '.png',
                      'wb') as zero:
                zero.write(res.content)
            Curiosity.topic_img_0_scr.append(
                './topics/zero-img-' + str(count) + '.png')
            count = count + 1
        return Curiosity.topic_img_0_scr

    @staticmethod
    # скачиваем 1-е изображение поста
    def img_1_downloader():
        count = 0
        max_index = len(Curiosity.topic_img_1_href) - 1
        while count <= max_index:
            res = requests.get(Curiosity.topic_img_1_href[count])
            with open('./topics/1-img-' + str(count) + '.png',
                      'wb') as zero:
                zero.write(res.content)
            Curiosity.topic_img_1_scr.append(
                './topics/1-img-' + str(count) + '.png')
            count = count + 1
        return Curiosity.topic_img_1_scr

    @staticmethod
    # скачиваем 2-е изображение поста
    def img_2_downloader():
        count = 0
        max_index = len(Curiosity.topic_img_2_href) - 1
        while count <= max_index:
            try:
                res = requests.get(Curiosity.topic_img_2_href[count])
                with open('./topics/2-img-' + str(count) + '.png',
                      'wb') as zero:
                    zero.write(res.content)
                #Curiosity.topic_img_2_scr.append(                '/home/ubuntu/workspac/curiosity-to-v/topics/two-img-' + str(count) + '.png')
            except:
                with open('./topics/2-img-' + str(count) + '.png',
                      'wb') as zero:
                    zero.close()
               #Curiosity.topic_img_2_scr.append("None")
            count = count + 1
        #return Curiosity.topic_img_2_scr

    @staticmethod
    # скачиваем 3-е изображение поста
    def img_3_downloader():
        count = 0
        max_index = len(Curiosity.topic_img_3_href) - 1
        while count <= max_index:
            try:
                res = requests.get(Curiosity.topic_img_3_href[count])
                with open('./topics/3-img-' + str(count) + '.png',
                      'wb') as zero:
                    zero.write(res.content)
                #Curiosity.topic_img_3_scr.append(                '/home/ubuntu/workspac/curiosity-to-v/topics/two-img-' + str(count) + '.png')
            except:
                with open('./3-img-' + str(count) + '.png',
                      'wb') as zero:
                    zero.close()
               #Curiosity.topic_img_3_scr.append("None")
            count = count + 1
        #return Curiosity.topic_img_3_scr

# ======ТЕСТЫ==========ТЕСТЫ===============ТЕСТЫ=============ТЕСТЫ==============
CuriosityTrendingparser.TrendingParser.change_href()
Curiosity.topic_img_0_alt = Curiosity.img_0_alt_parser()
Curiosity.topicsparser()
Curiosity.img_0_downloader()
Curiosity.translater()
Curiosity.painters()
Curiosity.img_1_downloader()
Curiosity.img_3_downloader()
Curiosity.img_2_downloader()
x = "ПАУЗА В ЧЕСТЬ УСПЕШНОГО ЗАВЕРШЕНИЯ"
print(x)
y = x
if __name__ == "__main__":
    print("Любопытcтво делает вас умнее")