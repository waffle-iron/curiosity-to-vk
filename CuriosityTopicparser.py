import re
import sys, os
import requests
from bs4 import BeautifulSoup

from CuriosityTrendingparser import TrendingParser


def topic_parser(href):

    # НАСТРАИВАЕМ ПАРСЕРА

    r = requests.get(href)

    html = r.text

    soup = BeautifulSoup(html, "lxml")

    topic_page = soup.find("div", {"class": "topic-page"})

    content_header = topic_page.find_all("div", {"class": "image-header"})

    topic_contents = topic_page.find("div", {"class": ["topic-content", "content-items"]})

    topic_content_item = topic_contents.find_all("div", {"class": "content-item"})

    regexp_img_1 = re.compile(r'/curiosity-data\.s3\.amazonaws\.com/images/content/hero/standard/(.*?)\.png\"\)')

    # ПАРСИМ

    # Головные данные
    for item in content_header:

        # ID 1-го изображения
        img_1_href = re.findall(regexp_img_1, item.find('style').text)

        # условия прохода если HTML топика с багами
        if item.find("div", {"class": "header-content"}).find('a') != None:

            # название канала
            channel = item.find("div", {"class": "header-content"}).find('a').text

            # заголовок топика
            title = item.find("div", {"class": "header-content"}).find('h1').text

        elif item.find("div", {"class": "header-content"}).find('a') == None:

            channel = item.find("div", {"class": "header-content"}).find('h5').text

            title = item.find("div", {"class": "header-content"}).find('h1').text

    # Данные в теле
    # основной текст топика
    text_1 = topic_content_item[1].text

    # ссылка на 2-е изображения
    try:
        img_2_href = topic_content_item[2].find("div", {"class": "embedded-graphic-content"}).find("img", {"class": "lazyload"})["data-src"]
    except AttributeError:
        img_2_href = None
        print(AttributeError)

    # заголовок 2-го параграфа
    try:
        paragraph_2_title = topic_content_item[3].find("div", {"class": ["section-header", "content-item-header"]}).text
    except AttributeError:
        paragraph_2_title = None
        print(AttributeError)
    # текст 2-го параграфа
    paragraph_2_text = topic_content_item[4].text
    # TODO: ПРОБЛЕМА: Главной приметой места разделения этого большого текста на параграфы, является пунктуационая ошибка - новое предложение, отделено от предидущего только точкой, а не точкой с пробелом.
    # TODO: РЕШЕНИЕ: разработать регулярное выражение выявляющее данный дефект и являющееся параметром функции split() применяемой к тексту во время репоста.

    # ссылка на 3-е изображение
    try:
        img_3_href = topic_content_item[5].find("div", {"class": "embedded-graphic-content"}).find("img", {"class": "lazyload"})["data-src"]
    except AttributeError:
        img_3_href = None
        print(AttributeError)
    # заголовок 3- го параграфа
    try:
        paragraph_3_title = topic_content_item[6].find("div", {"class": ["section-header", "content-item-header"]}).text
    except AttributeError:
        paragraph_3_title = None
        print(AttributeError)

    # текст 3-го параграфа
    try:
        paragraph_3_text = topic_content_item[7].text
    except:
        paragraph_3_text = None
    # заголовок видеоролика
    try:
        video_1_title = topic_content_item[10].find("div", {"class": ["first-video", "content-item-header"]}).find("h4").text
    except:
        video_1_title = None
        pass
    # ID видеоролика
    try:
        video_1_data_scr = topic_content_item[10].find("div", {"class": "first-video"}).find("div", {"class": "module-video"}).find("div", {"class": "js-media-player"})["data-src"]
    except:
        video_1_data_scr = None
        pass

    return img_1_href, channel, title, text_1, img_2_href, paragraph_2_title, paragraph_2_text, img_3_href, paragraph_3_title, paragraph_3_text, video_1_title, video_1_data_scr


if __name__ == "__main__":
    print("Парсимс")