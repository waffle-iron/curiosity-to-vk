import requests
import re
from grab import Grab
import trendingparser


topic_img_0_href = []
topic_img_0_scr = []
topic_img_0_hrefs = []
re_zero_img = re.compile(r'https://curiosity-data\.s3\.amazonaws\.com/images/content/meme/standard/(.*?)\.png')


def img_0_downloader():

    #скачиваем изображения обложек постов

    print(re_zero_img)
    respon = requests.get("http://curiosity.com/trending/")
    html = respon.text
    zero_img_srcs = re.findall(re_zero_img, html)
    for x in set(zero_img_srcs):
        topic_img_0_hrefs.append(x)
    print(zero_img_srcs)
    count = 0
    max_ind = len(topic_img_0_hrefs) - 1
    while count <= max_ind:
        topic_img_0_href.append("http://curiosity-data.s3.amazonaws.com/images/content/meme/standard/"+topic_img_0_hrefs[count]+".png")
        print(topic_img_0_href)
        res = requests.get(topic_img_0_href[count])
        with open('/home/ubuntu/workspace/curiosity-to-vk/topics/zero-img-'+str(count)+'.png', 'wb') as zero:
            zero.write(res.content)
        topic_img_0_scr.append('/home/ubuntu/workspac/curiosity-to-v/topics/zero-img-'+str(count)+'.png')
        count = count + 1

#========ТЕСТЫ=======ТЕСТЫ=========ТЕСТЫ=========ТЕСТЫ========#

img_0_downloader()

if __name__ == "__main__":
    print('download')


