import grab
from grab import Grab
#import curiostry

key = "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1"

g = Grab()

resp = g.go('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1', post={"text": "sub scrip table", 'lang': 'ru', 'format': 'plain'})

print(resp.unicode_body(ignore_errors=True, fix_special_entities=True))