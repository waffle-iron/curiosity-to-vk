import requests
import re
from grab import Grab
import trendingparser

from PIL import Image, ImageFont, ImageDraw, ImageEnhance
#from topicsparser import Curiosity
#from topicsparser import Curiosity

def painter():
    channel = "Удивительная планета"#topic_channel_ru[0][0]
    loader = Image.new()
    img = Image.open("./topics/zero-img-0.png").convert("RGBA")
    logo = Image.open('./topics/logo (1).png').convert('RGBA')
    logo_draw = ImageDraw.Draw(logo)
    img_draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./topics/Roboto-Fosts/Roboto-Regular.ttf", 14)
    channel_size = font.getsize(channel)
    _size = (channel_size[0], channel_size[1])
    channel_img = Image.new('RGBA', channel_size, )
    channel_draw = ImageDraw.Draw(channel_img)
    #channel_draw.multiline_text((0, 0), channel, font=font, align = "center")
    img.paste(channel_img, (10, 910))
    img.paste(logo, (1, 1))
    compositeon = Image.alpha_composite(img, bu)
    compositeon.save("./topics/zero-img-0-composit.png")
    channel_draw.channel((20, 20), channel, (186, 85, 100), font=font)
    img.save('./topics/zero-img-0-paint.png')


#========ТЕСТЫ=======ТЕСТЫ=========ТЕСТЫ=========ТЕСТЫ========#

painter()

if __name__ == "__main__":
    print('download')


