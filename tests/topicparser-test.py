from CuriosityTrendingparser import TrendingParser as TrendingParser
import CuriosityTopicparser
import os
import redis

# ТУЧА С ДАННЫМИ

topic_img_1_href = []
topic_channel = []
topic_title = []
topic_text_1 = []
topic_img_2_href = []
topic_paragraph_2_title = []
topic_paragraph_2_text = []
topic_img_3_href = []
topic_paragraph_3_title = []
topic_paragraph_3_text = []
topic_video_1_title = []
topic_video_1_data_scr = []

# ==========TEST================TEST======================TEST============== #

in_db, new, to_post = TrendingParser.change_href()
# TODO ТЕСТЫ НА ТЕСТЫ ПОКА НЕ ПОХОЖИ, ПРОРАБОТАТЬ
for href in new:
    try:
       img_1_href,channel,title,text_1, img_2_href, paragraph_2_title, paragraph_2_text, img_3_href, paragraph_3_title, paragraph_3_text, video_1_title, video_1_data_scr = CuriosityTopicparser.topic_parser(href)

       # ЗАПОЛНЯЕМ СПИСКИ
       # каналы
       topic_channel.append(str(channel))

       # заголовки
       topic_title.append(str(title))

       # ссылок на 1 изображения
       topic_img_1_href.append(
           "http://curiosity-data.s3.amazonaws.com/images/content/hero/standard/" + img_1_href[0] + ".png")

       # текты первых блоков
       topic_text_1.append(str(text_1))

       # ссылки на 2 изображения
       topic_img_2_href.append(str(img_2_href))

       # заголовки вторых параграфов
       topic_paragraph_2_title.append(str(paragraph_2_title))

       # тексты 2-х параграфов
       topic_paragraph_2_text.append(str(paragraph_2_text))

       # ссылки на 3 изображения
       topic_img_3_href.append(str(img_3_href))

       # заголовки третьих параграфов
       topic_paragraph_3_title.append(str(paragraph_3_title))

       # тексты 3-их параграфов
       topic_paragraph_3_text.append(str(paragraph_3_text))

       # заголовки видеороликов
       topic_video_1_title.append(str(video_1_title))

       # ссылки на видеоролики
       topic_video_1_data_scr.append(str(video_1_data_scr))

    except:
        print("Ошибочка выскочила")


print("СТОПАК-ДЛЯ-ДЕБАГ")



if __name__ == "__main__":
    print("Парсимс")