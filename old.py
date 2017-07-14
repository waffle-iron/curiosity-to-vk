import requests
import re
from grab import Grab

html = requests.get("https://curiosity.com/trending/").text
with open("./html_trending.html", "w") as file:
    file.write(html)

re_front_img_src = re.compile(r'/curiosity-data\.s3\.amazonaws\.com/images/content/hero/standard/(.*?)\.png\"\)')



if __name__ == "__main__":
    print('download')
    
    
    