import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup


def img_0_downloader():
    respon = requests.get("http://curiosity.com/trending/")
    html = respon.text
    soup = BeautifulSoup(html, "lxml")
    trending_grid = soup.find("div", {"class": "js-trending-grid"})
    all_a = trending_grid.find_all("a")
    href = []
    import re
    for item in all_a:
        img = item.find("img")
        img = str(img["src"])
        href.append(img)
    count = 0
    max_ind = len(href) - 1
    while count <= max_ind:
        res = requests.get(str(href[count]))
        with open('C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/0-img-' + str(count) + '.png',
                  'wb') as zero:
            zero.write(res.content)
        #Curiosity.topic_img_0_scr.append('/home/ubuntu/workspac/curiosity-to-v/topics/zero-img-' + str(count) + '.png')
        count = count + 1
    return href

href = img_0_downloader()
x=0