# -*- coding: utf-8 -*-

import logging
import requests
import re
import json
from bs4 import BeautifulSoup
import CuriosityTrendingparser


logging.basicConfig(level=logging.DEBUG)


class Curiosity:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


    @staticmethod
    def get_href():
        href_in_db, href_new, href_to_post = CuriosityTrendingparser.TrendingParser.change_href()

    class Topics:

        def __init__(self, topic_href, subjects_href, subjects_channel1, title, img1, text_section1, img2, text_section2, video1, *args, **kwargs):
            self.topic_href = topic_href
            self.subjects_href = subjects_href
            self.subjects_channel1 = subjects_channel1
            self.title = title
            self.img1 = img1
            self.text_section1 = text_section1
            self.img2 = img2
            self.text_section2 = text_section2
            self.video1 = video1
            self.args = args
            self.kwargs = kwargs



if __name__ == '__main__':
    print('Модуль Cutiosity импортирован')