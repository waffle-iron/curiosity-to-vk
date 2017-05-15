# -*- coding: utf-8 -*-
import grab
from grab import Grab
import re
import os
import base64
import urllib3
from base64 import b64encode
from six.moves.urllib.parse import urlencode, urljoin


topics = []
href = []
title = []
front_img_src = []
front_img_alt = []
landimg =[]
trumbimg = []
description = []
video = []
tags = []
links = []

re_href = re.compile(r'.a\shref=\"/topics/(.*?)/\"\n')
re_title= re.compile(r'title=\"(.*?)\">')
re_front_img_src = re.compile(r'src=\"https://dw8stlw9qt0iz\.cloudfront\.net/(.*?)/fit-in/380x0/filters:format\(jpeg\):quality\(70\)/https:(.*?)\"')
re_front_img_alt = re.compile(r'alt=\"(.*?)\"')


def curi_tr_get_html():
    '''Возвращает html страницы трендов'''
    trendings_html = ""
    g = Grab(timeout=20)
    resp = g.go("https://curiosity.com/trending/")
    trendings_html = resp.unicode_body(ignore_errors=True, fix_special_entities=True)
    return trendings_html

def curi_tr_html_get_topic_href():
    '''Возвращает список ссылок на посты'''
    hrefs = re.findall(re_href, curi_tr_get_html())
    count = 0
    max_index = 9
    while count <= max_index:
        href.append("http://curiosity.com/topics/" + hrefs[count] + "/")
        count = count + 1
    return href

def curi_tr_get_topic_title():
    '''Возвращает список заголовков постов'''
    titels = re.findall(re_title, curi_tr_get_html())
    count = 0
    max_index = 9
    while count <= max_index:
        title.append("" + titels[count] + "")
        count = count + 1
    return title

def curi_tr_get_topic_front_img_alt():
    '''Возвращает список описаний главных изображений'''
    front_img_alts = re.findall(re_front_img_alt, curi_tr_get_html())
    count = 0
    max_index = 9
    while count <= max_index:
        front_img_alt.append("" + front_img_alts[count] + "")
        count = count + 1
    return front_img_alt

def curi_tr_download_topic_front_img():
    '''Скачивает главные изображения постов'''
    front_img_srcs = re.findall(re_front_img_src, curi_tr_get_html())
    g_front_img = Grab(timeout=20)
    g_front_img.setup(headers={'chrome-proxy': 's=Ci4KEwjMhrTr79_TAhXQIBkKHQH0A0USDAib-sXIBRCojrrZAxoJCgdkZWZhdWx0EkgwRgIhAIdAgOu3URu5cs-VjgT5MlOXD8ckBB3udUqTMeXYIGc0AiEAmdK5TxX33uuUGLrtjrZGzKNXOnV4NIJg6YKU50BVMsA=, c=win, b=3029, p=96'})
    count = 0
    max_index = 9
    while count <= max_index:
        front_img_src.append("http:" + front_img_srcs[count][1])
        resp = g_front_img.go(front_img_src[count])
        open('./curiosity-to-vk/front_img/front_img'+str(count)+'.png', 'wb').write(resp.body)
        front_img_src.append('./curiosity-to-vk/front_img/front_img'+str(count)+'.png')
        count = count + 1
    return front_img_src

class Topics:
    def __init__(self, href, title, front_img_src, front_img_alt):
        self.href = href
        self.title = title
        self.front_img_src = front_img_src
        self.front_img_alt = front_img_alt

def topic_obj_gen():
    count = 0
    max_index = range(9)
    for count in max_index:
        yield Topics(curi_tr_html_get_topic_href()[count], curi_tr_get_topic_title()[count], curi_tr_download_topic_front_img()[count], curi_tr_get_topic_front_img_alt()[count])

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

#generation_topic()
#print(topics[8].title)

if __name__ == "__main__":
    print("Любопытство[curiosity.com]")