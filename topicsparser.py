# -*- coding: utf-8 -*-

import logging
import requests
import re
import json
from bs4 import BeautifulSoup
import trendingparser
from trendingparser import TrendingParser





class TopicsParser:
    in_db, new, to_post = TrendingParser.change_href()

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


    @staticmethod
    def get_topic():
        for href in TopicsParser.new:
            r = requests.get(href)
            html = r.text
            #print(html)
            soup = BeautifulSoup(html, "lxml")
            topic_page = soup.find("div", {"class": "topic-page"})
            image_header = topic_page.find_all("div", {"class": "image-header"})
            for item in image_header:
                if item.find("div", {"class": "header-content"}).find('a') != None:
                    subject_channel = item.find("div", {"class": "header-content"}).find('a').text
                    title = item.find("div", {"class": "header-content"}).find('h1').text
                elif item.find("div", {"class": "header-content"}).find('a') == None:
                    subject_channel = item.find("div", {"class": "header-content"}).find('h5').text
                    title = item.find("div", {"class": "header-content"}).find('h1').text

                print(f'Канал: {subject_channel}. Тема: {title}')

TopicsParser.get_topic()
if __name__ == "__main__":
    print("parse_topics")