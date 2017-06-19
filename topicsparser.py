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


in_db, new, to_post = TrendingParser.change_href()

for href in new:

    r = requests.get(href)

    html = r.text

    soup = BeautifulSoup(html, "lxml")

    topic_page = soup.find("div", {"class": "topic-page"})

    head = topic_page.find_all("div", {"class": "image-header"})

    body = topic_page.find_all("div", {"class": "content-item"})

    regexp_img1 = re.compile(r'/curiosity-data\.s3\.amazonaws\.com/images/content/hero/standard/(.*?)\.png\"\)')

    for item in head:
        img1 = re.findall(regexp_img1, item.find('style').text)
        if item.find("div", {"class": "header-content"}).find('a') != None:

            subject_channel = item.find("div", {"class": "header-content"}).find('a').text

            title = item.find("div", {"class": "header-content"}).find('h1').text

        elif item.find("div", {"class": "header-content"}).find('a') == None:

            subject_channel = item.find("div", {"class": "header-content"}).find('h5').text

            title = item.find("div", {"class": "header-content"}).find('h1').text

    text1 = body[0].find("p").text


    print(f"Channel: {subject_channel}." + "\n" + f"Title: {title}."+ "\n" + f"Image: {img1[0]}." + "\n" + f"Description: {text1}.")


if __name__ == "__main__":
    print("parse_topics")