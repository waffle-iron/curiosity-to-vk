from __future__ import print_function
import requests
import re
from grab import Grab
import CuriosityTrendingparser
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

#from topicsparser import Curiosity


def painter(count):

    # TODO: ДОБАВИТ В СКРИПТЕ ЗАПУСКА цикл для прохода по всем изображения. Сделать плюсом к англо-руской обложке полностью русская обложка из третьего изоброжения топика

    # Название канала
    channel = "Психология.".upper()  # topic_channel_ru[0][0]

    # Заголовок
    title = "Как Нарисовать Круг Связана С Культурным Воспитанием."

    # изображение для модификации
    img_composit = Image.open("./topics/zero-img-"+str(count)+".png").convert("RGBA")

    # прозрачный загрузчик логотипов
    logo_painter = Image.open('./logo-playload.png').convert("RGBA")

    # кисть для загрузчика
    logo_painter_draw = ImageDraw.Draw(logo_painter)

    # шрифты
    channel_font = ImageFont.truetype("./topics/Roboto-Fosts/Roboto-Bold.ttf", 24)

    # размер блока текста с названием канала в списке
    channel_size = channel_font.getsize(channel)

    # размер блока текста с названием канала в кортеже
    _size = (channel_size[0] + 20, channel_size[1] + 20)

    # пустые изображение для нанесения текста с названием канала
    channel_im = Image.open('./Button.png').convert("RGBA")

    # изменяем размер изображения
    channel_img = channel_im.resize(_size, resample=0)

    # кисть для пустое изображение для нанесения текста с названием канала
    channel_draw = ImageDraw.Draw(channel_img)

    # процедура нанесения мультистрокового текста с названием канала на изобрание
    x = (_size[0] - channel_size[0]) / 2
    y = (_size[1] - channel_size[1]) / 2
    channel_draw.multiline_text((x, y), channel, font=channel_font, align="center")

    # наносим заголовок на загрузцик
    logo_painter_draw.multiline_text((10, 945), title, font=channel_font, align="left")

    # наносим канал и заголовок на загрузчик
    logo_painter.paste(channel_img, (5, 900))

    # композиция обложки и загрузчика логотипов
    composition = Image.alpha_composite(img_composit, logo_painter)

    # процедура сохранения композиционной обложки в файл
    composition.save("./topics/zero-img-"+str(count)+"-composite.png")  # compositeon.save("./topics/zero-img-0-composit.png")

# ========ТЕСТЫ=======ТЕСТЫ=========ТЕСТЫ=========ТЕСТЫ========

count = 0
max_index = 9
while count <= max_index:
    painter(count)
    count = count + 1

print("Cтоп брейк")


if __name__ == "__main__":
    print("Художничаемс")
    #  Image.open("C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/").convert("RGBA")