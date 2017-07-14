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
    front_img = []
    title_ru = []
    first_post_img_href = []
    first_post_img = []
    landimg =[]
    trumbimg = []
    descriptions = []
    descriptions_ru =[]
    video = []
    tags = []
    links = []
    full_topic_html = []
    first_img_src = []
    first_img_href = []
    post_lists = []
    first_img = []

    # Регулярные выражения для разбора html
    re_href = re.compile(r'.a\shref=\"/topics/(.*?)/\"\n')
    re_title= re.compile(r'title=\"(.*?)\">')
    re_front_img_src = re.compile(r'/curiosity-data\.s3\.amazonaws\.com/images/content/hero/standard/(.*?)\.png\"\)')
    re_front_img_alt = re.compile(r'alt=\"(.*?)\"')
    re_first_post_img = re.compile(r'<img class="flipboard-image" src="https://dw8stlw9qt0iz.cloudfront.net/(.*?)/750x450/filters:format\(jpeg\):quality\(75\)/(.*?)\"')
    re_description = re.compile(r'')

url\(\"https://dw8stlw9qt0iz\.cloudfront\.net/(.*?)/1000x600/filters:format\(jpeg\):quality\(80\):extract_focal\(\)/(.*?)\.png\"\)

    def __init__(self, href, title, front_img_alt, front_img_alt_ru, title_ru, front_img, first_img, descriptions, descriptions_ru):
        #Метод инициализации объекта класса
        self.href = href
        self.title = title
        #self.front_img_src = front_img_src
        self.front_img_alt = front_img_alt
        self.front_img_alt_ru = front_img_alt_ru
        self.title_ru = title_ru
        self.front_img = front_img
        self.first_post_img = first_img
        self.descriptions = descriptions
        self.descriptions_ru = descriptions_ru


    @staticmethod
    def curi_tr_html_get_topic_href():
        #'''Возвращает список ссылок на посты'''
        with open("./my_href.db") as database:
            for line in database:
                Topics.href.append(line)
            return Topics.href


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
    def curi_tr_get_topic_title():
        #'''Возвращает список заголовков постов'''
        with open('/home/ubuntu/workspace/curiosity-to-vk/curi_rt_html.html') as f:
            text = f.read()
        count = 0
        max_index = 9
        soup = BeautifulSoup(text, 'lxml')
        items = soup.find_all( 'a', {'class': 'trending-grid-item'})
        for item in items:
            title = item.get('title')
            Topics.title.append(title)
        return Topics.title


    @staticmethod
    def curi_tr_get_topic_front_img_alt():
        #'''Возвращает список описаний главных изображений'''
        count = 0
        max_index = 9
        text = open('/home/ubuntu/workspace/curiosity-to-vk/curi_rt_html.html').read()
        soup = BeautifulSoup(text, 'lxml')
        items = soup.find_all( 'a', {'class': 'trending-grid-item'})
        for item in items:
            alt = item.find().get('alt')
            Topics.front_img_alt.append(alt)


    @staticmethod
    def download_front_img():
        #Скачивает главные изображения постов'''
        with open('/home/ubuntu/workspace/curiosity-to-vk/curi_rt_html.html') as f:
            text = f.read()
        Topics.front_img_srcs = re.findall(Topics.re_front_img_src, text)
        g_front_img = Grab(timeout=20)
        g_front_img.setup(headers={'chrome-proxy': 's=Ci4KEwjMhrTr79_TAhXQIBkKHQH0A0USDAib-sXIBRCojrrZAxoJCgdkZWZhdWx0EkgwRgIhAIdAgOu3URu5cs-VjgT5MlOXD8ckBB3udUqTMeXYIGc0AiEAmdK5TxX33uuUGLrtjrZGzKNXOnV4NIJg6YKU50BVMsA=, c=win, b=3029, p=96'})
        count = 0
        max_index = 9
        while count <= max_index:
            Topics.front_img_href.append("http:" + Topics.front_img_srcs[count][1])
            resp = g_front_img.go(Topics.front_img_href[count])
            open('/home/ubuntu/workspace/curiosity-to-vk/topics/front-img-'+str(count)+'.png', 'wb').write(resp.body)
            Topics.front_img.append('/home/ubuntu/workspace/curiosity-to-vk/topics/front-img/'+str(count)+'.png')
            count = count + 1
        return Topics.front_img


    @staticmethod
    def get_first_img_src():
        g_first_post_img = Grab(timeout=20)
        g_first_post_img.setup(headers={'chrome-proxy': 's=Ci4KEwjMhrTr79_TAhXQIBkKHQH0A0USDAib-sXIBRCojrrZAxoJCgdkZWZhdWx0EkgwRgIhAIdAgOu3URu5cs-VjgT5MlOXD8ckBB3udUqTMeXYIGc0AiEAmdK5TxX33uuUGLrtjrZGzKNXOnV4NIJg6YKU50BVMsA=, c=win, b=3029, p=96'})
        count = 0
        max_index = 9
        #Topics.curi_get_full_topic_html()
        while count <= max_index:
            with open('/home/ubuntu/workspace/curiosity-to-vk/topics/html/'+str(count)+'.html') as f:
                text = f.read()
            re_string = re.findall(Topics.re_first_post_img, text)
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
            Topics.first_img.append('/home/ubuntu/workspace/curiosity-to-vk/topics/first-img/'+str(count)+'.jpg')
            count = count + 1


    @staticmethod
    def get_descriptions():
        count = 0
        max_index = 9
        while count <= max_index:
            text = open('/home/ubuntu/workspace/curiosity-to-vk/topics/html/'+ str(count) + '.html')
            soup = BeautifulSoup(text, 'lxml')
            Topics.descriptions.append(soup.find('div', {'class': 'description'}).find('p').text)
            count = count + 1
        return Topics.descriptions


    @staticmethod
    def transya():
        #Перевод на русский язык. Спасибо яндекс переводчику ! :)
        g_translate_img_alt = Grab()
        g_translate_img_title = Grab()
        g_translate_description = Grab()
        count = 0
        max_index = len(Topics.href)
        for count in range(9):
            #Переводим описание изображения
            resp_front_img_alt_ru = json.loads(g_translate_img_alt.go('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1', post={"text": Topics.curi_tr_get_topic_front_img_alt()[count], 'lang': 'en-ru', 'format': 'plain'}).unicode_body(ignore_errors=True, fix_special_entities=True))
            Topics.front_img_alt_ru.append(str(resp_front_img_alt_ru))
            #Переводим титул постов
            resp_title_ru = json.loads(g_translate_img_title.go('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1', post={"text": Topics.curi_tr_get_topic_title()[count], 'lang': 'en-ru', 'format': 'plain'}).unicode_body(ignore_errors=True, fix_special_entities=True))
            Topics.title_ru.append(str(resp_title_ru["text"]))
            #Переводим расширенное описание поста
            resp_descriptions_ru = json.loads(g_translate_img_alt.go('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1', post={"text": Topics.get_descriptions()[count], 'lang': 'en-ru', 'format': 'plain'}).unicode_body(ignore_errors=True, fix_special_entities=True))
            Topics.descriptions_ru.append(str(resp_descriptions_ru["text"]))
            count = count + 1


    @staticmethod
    def topic_obj_gen():
        count = 0
        max_index = range(1)
        for count in max_index:
            yield Topics(Topics.curi_tr_html_get_topic_href()[count], curi_tr_get_topic_title()[count], download_front_img()[count], curi_tr_get_topic_front_img_alt()[count], )
            #href, title, front_img_src, front_img_alt, front_img_alt_ru, title_ru, first_img, descriptions, descriptions_ru


    @staticmethod
    def generation_topic():
        con = 0
        max_index = 1
        topic_gen = topic_obj_gen()
        for count in topic_gen:
            if con <= max_index:
                topic = Topics(href[con], title[con], front_img_src[con], front_img_alt[con])
                topics.append(topic)
                con += 1
        return topics

if __name__ == '__main__':
    print('Модуль Cutiosity импортирован')