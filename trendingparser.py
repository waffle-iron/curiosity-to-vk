import requests
from bs4 import BeautifulSoup



class TrendingParser:

    def __init__(self, in_db, new, to_post):
        self.in_db = in_db
        self.new = new
        self.to_post = to_post


    @staticmethod
    def change_href():
        path_my_href = './my_href.db'
        href_new = []
        href_in_db = []
        href_to_post = []
        with open(path_my_href) as database:
            for line in database:
                href_in_db.append(line.replace('\n', ''))
        r = requests.get("https://curiosity.com/trending/")
        text = r.text
        soup = BeautifulSoup(text, 'lxml')
        items = soup.find_all( 'a', {'class': 'trending-grid-item'})
        for item in items:
            href = item.get('href')
            href_new.append(str('http://curiosity.com' + href))
        for href in set(href_new).difference(href_in_db):
            href_to_post.append(href)
        with open(path_my_href, 'a') as f:
            for line in href_to_post:
                f.write(str(line) + '\n')
            if len(href_to_post) != 0:
                with open('./href-to-post.db', 'w') as h:
                    for line in href_to_post:
                        h.write(str(line) + '\n')
        return href_in_db, href_new, href_to_post


if __name__ == "__main__":
    print("refresh_links")