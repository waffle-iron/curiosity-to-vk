# -*- coding: utf-8 -*-

import logging
from grab import Grab
import re
import json
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)
class Topics:
    #Описание поста как объекта
        #Базовые переменные
    topics = []
    href = []
    title = []
    front_img_href = []
    front_img_src = []
    front_img_alt = []
    front_img_alt_ru = []
    title_ru = []
    first_post_img_href = []
    first_post_img = []
    landimg =[]
    trumbimg = []
    description = []
    video = []
    tags = []
    links = []
    full_topic_html = []
    first_img_src = []
    first_img_href = []

    re_href = re.compile(r'.a\shref=\"/topics/(.*?)/\"\n')
    re_title= re.compile(r'title=\"(.*?)\">')
    re_front_img_src = re.compile(r'src=\"https://dw8stlw9qt0iz\.cloudfront\.net/(.*?)/fit-in/380x0/filters:format\(jpeg\):quality\(70\)/https:(.*?)\"')
    re_front_img_alt = re.compile(r'alt=\"(.*?)\"')
    re_first_post_img = re.compile(r'<img class="flipboard-image" src="https://dw8stlw9qt0iz.cloudfront.net/(.*?)/750x450/filters:format\(jpeg\):quality\(75\)/(.*?)\"')
    re_description = re.compile(r'')

    def __init__(self, href, title, front_img_src, front_img_alt, front_img_alt_ru, title_ru, first_post_img):
        #Метод инициализации объекта класса
        self.href = href
        self.title = title
        self.front_img_src = front_img_src
        self.front_img_alt = front_img_alt
        self.front_img_alt_ru = front_img_alt_ru
        self.title_ru = title_ru
        self.first_post_img = first_post_img

    @staticmethod
    def curi_tr_get_html():
        #'''Возвращает html страницы трендов'''
        trendings_html = ""
        g = Grab(timeout=20)
        resp = g.go("https://curiosity.com/trending/")
        trendings_html = resp.unicode_body(ignore_errors=True, fix_special_entities=True)
        open('/home/ubuntu/workspace/curiosity-to-vk/curi_rt_html.html', 'w').write(trendings_html)
        return trendings_html

    @staticmethod
    def get_full_topic_html():
        count = 0
        max_index = 9
        g_full_topic_html = Grab()
        while count <= max_index:
            resp = g_full_topic_html.go(Topics.curi_tr_html_get_topic_href()[count])
            Topics.full_topic_html.append(resp.unicode_body(ignore_errors=True, fix_special_entities=True))
            open('/home/ubuntu/workspace/curiosity-to-vk/topics/html/'+str(count)+'.html', 'w').write(Topics.full_topic_html[count])
            count = count + 1
        return Topics.full_topic_html

    @staticmethod
    def curi_tr_html_get_topic_href():
        #'''Возвращает список ссылок на посты'''
        hrefs = re.findall(Topics.re_href, Topics.curi_tr_get_html())
        count = 0
        max_index = 9
        while count <= max_index:
            Topics.href.append("http://curiosity.com/topics/" + hrefs[count] + "/")
            count = count + 1
        return Topics.href

    @staticmethod
    def curi_tr_get_topic_title():
        #'''Возвращает список заголовков постов'''
        Topics.titels = re.findall(Topics.re_title, Topics.curi_tr_get_html())
        count = 0
        max_index = 9
        while count <= max_index:
            Topics.title.append("" + Topics.titels[count] + "")
            count = count + 1
        return Topics.title

    @staticmethod
    def curi_tr_get_topic_front_img_alt():
        #'''Возвращает список описаний главных изображений'''
        Topics.front_img_alts = re.findall(Topics.re_front_img_alt, Topics.curi_tr_get_html())
        #soup  = BeautifulSoup(Topics.curi_tr_get_html(), 'lxml')
        #front_img_alts = soup.find()
        count = 0
        max_index = 9
        while count <= max_index:
            Topics.front_img_alt.append("" + Topics.front_img_alts[count] + "")
            count = count + 1
        print(Topics.front_img_alt)
        return Topics.front_img_alt

    @staticmethod
    def download_front_img():
        #Скачивает главные изображения постов'''
        Topics.front_img_srcs = re.findall(Topics.re_front_img_src, Topics.curi_tr_get_html())
        g_front_img = Grab(timeout=20)
        g_front_img.setup(headers={'chrome-proxy': 's=Ci4KEwjMhrTr79_TAhXQIBkKHQH0A0USDAib-sXIBRCojrrZAxoJCgdkZWZhdWx0EkgwRgIhAIdAgOu3URu5cs-VjgT5MlOXD8ckBB3udUqTMeXYIGc0AiEAmdK5TxX33uuUGLrtjrZGzKNXOnV4NIJg6YKU50BVMsA=, c=win, b=3029, p=96'})
        count = 0
        max_index = 9
        while count <= max_index:
            Topics.front_img_href.append("http:" + Topics.front_img_srcs[count][1])
            resp = g_front_img.go(Topics.front_img_href[count])
            open('/home/ubuntu/workspace/curiosity-to-vk/topics/front-img/'+str(count)+'.png', 'wb').write(resp.body)
            Topics.front_img_src.append('/home/ubuntu/workspace/curiosity-to-vk/topics/front-img/'+str(count)+'.png')
            count = count + 1
        return Topics.front_img_src

    @staticmethod
    def get_first_img_src():
        g_first_post_img = Grab(timeout=20)
        g_first_post_img.setup(headers={'chrome-proxy': 's=Ci4KEwjMhrTr79_TAhXQIBkKHQH0A0USDAib-sXIBRCojrrZAxoJCgdkZWZhdWx0EkgwRgIhAIdAgOu3URu5cs-VjgT5MlOXD8ckBB3udUqTMeXYIGc0AiEAmdK5TxX33uuUGLrtjrZGzKNXOnV4NIJg6YKU50BVMsA=, c=win, b=3029, p=96'})
        count = 0
        max_index = 9
        #Topics.curi_get_full_topic_html()
        while count <= max_index:
            re_string = re.findall(Topics.re_first_post_img, Topics.full_topic_html[count])
            Topics.first_img_src.append(re_string[0][1])
            count = count + 1
        return Topics.first_img_src

    @staticmethod
    def download_first_img():
        count = 0
        max_index = 9
        g_first_img = Grab(timeout=20)
        g_first_img.setup(headers={'chrome-proxy': 's=Ci4KEwjMhrTr79_TAhXQIBkKHQH0A0USDAib-sXIBRCojrrZAxoJCgdkZWZhdWx0EkgwRgIhAIdAgOu3URu5cs-VjgT5MlOXD8ckBB3udUqTMeXYIGc0AiEAmdK5TxX33uuUGLrtjrZGzKNXOnV4NIJg6YKU50BVMsA=, c=win, b=3029, p=96'})
        hrefs = []
        hrefs = Topics.get_first_img_src()
        while count <= max_index:
            Topics.first_img_href.append("http://" + hrefs[count])
            resp = g_first_img.go(Topics.first_img_href[count])
            open('/home/ubuntu/workspace/curiosity-to-vk/topics/first-img/'+str(count)+'.jpg', 'wb').write(resp.body)
            count = count + 1

    @staticmethod
    def get_description():
        soup = BeautifulSoup(Topics.get_full_topic_html(), 'lxml')
        descriptions = soup.find('div', {'class': 'description'}).find('p').text
        print(descriptions)

    @staticmethod
    def transya():
        #Перевод на русский язык. Спасибо яндекс переводчику ! :)
        g_translate_img_alt = Grab()
        g_translate_img_title = Grab()
        count = 0
        max_index = len(Topics.href)
        for count in range(9):
            #Переводим описание изображения
            Topics.front_img_alt_ru = json.loads(g_translate_img_alt.go('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1', post={"text": Topics.curi_tr_get_topic_front_img_alt()[count], 'lang': 'en-ru', 'format': 'plain'}).unicode_body(ignore_errors=True, fix_special_entities=True))
            #Переводим титул постов
            resp_tr_title = json.loads(g_translate_img_title.go('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1', post={"text": Topics.curi_tr_get_topic_title()[count], 'lang': 'en-ru', 'format': 'plain'}).unicode_body(ignore_errors=True, fix_special_entities=True))
            Topics.title_ru.append(str(resp_tr_title["text"]))
            count = count + 1

    @staticmethod
    def topic_obj_gen():
        count = 0
        max_index = range(9)
        for count in max_index:
            yield Topics(curi_tr_html_get_topic_href()[count], curi_tr_get_topic_title()[count], download_front_img()[count], curi_tr_get_topic_front_img_alt()[count], )

    @staticmethod
    def generation_topic():
        con = 0
        max_index = 9
        topic_gen = topic_obj_gen()
        for count in topic_gen:
            if con <= max_index:
                topic = Topics(href[con], title[con], front_img_src[con], front_img_alt[con])
                topics.append(topic)
                con += 1
        return topics



#Topics.get_full_topic_html()
#Topics.get_first_img_src()
#Topics.download_first_img()
#Topics.download_front_img()
Topics.curi_tr_get_topic_front_img_alt()
print(Topics.curi_tr_get_topic_title())