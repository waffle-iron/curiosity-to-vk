import grab
from grab import Grab
import curiosity
from curiosity import Topics
import pyrebase

    



if __name__ == '__main__':
    print('Переводчик постов успешно завершил работу')


'''
resp_translates_dict = g_translates_dict.go('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?k=dict.1.1.20170515T065130Z.2f91c55c3a4bde62.ac660eaa245416d41b3ba2f565f732320e7bd8aa', post={'lang': '-en', "text": curiosity.topics[count].front_img_alt, 'ui': 'ru'}).body
open('/home/ubuntu/workspace/curiosity-to-vk/translate_texts/power_translate_text'+str(count)+'.json', 'w').write(resp_translates_dict)
'''