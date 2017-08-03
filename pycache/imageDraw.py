from bs4 import BeautifulSoup
#from lxml import html
import PIL
from PIL import Image
from PIL import ImageDraw
import curiosity

# get an image
base = Image.open('/home/ubuntu/workspace/curiosity-to-vk/topics/first-img/4.png').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
#txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
#PIL.ImageDraw.Draw.setfontfont)
# get a drawing context
#d = ImageDraw.Draw()
txt = curiosity.title_ru[0]
ImageDraw.Draw.multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="center")

out = Image.alpha_composite(base, txt)


'''
text = open('./req_test.html', 'rt')
soup = BeautifulSoup(text, "lxml")
description_href = soup.find('div', {'class': 'description'}).find('a').get("href")
description_text = soup.find('div', {'class': 'description'}).find('p').text
capute = soup.find('div', {'class': 'caption'})
capute_to_print = capute.ljust


img = Image.open("./curiosity-to-vk/topics/first-img/0.png", "r")
draw = ImageDraw.Draw(img)
print(draw)
#font = ImageFont.truetype(1200, 628)
font = ImageFont.truetype("./curiosity-to-vk/topics/Roboto-Fosts/Roboto-Regular.ttf", 16)
#draw.text((x, y),str(capute),(r,g,b))
draw.text((20, 20),capute.split("."),(186, 85, 211),font=font)
img.save('./curiosity-to-vk/topics/first-img/0.png')
'''


        #составляем текст
        txt = f"{Curiosity.topic_channel_ru[0][0]}" + "\n" + f"{Curiosity.topic_text_1_ru[0][0]}" + "\n" + f"{Curiosity.topic_title_ru[0][0]}"
        #открываем изоброжение
        base = Image.open('/home/ubuntu/workspace/curiosity-to-vk/topics/0.png').convert('RGBA')
        #наносим текст на изображение
        PIL.ImageDraw.Draw.multiline_text(11, txt, fill=None, font=None, anchor=None, spacing=0, align="center")

        out = Image.alpha_composite(base, txt)

        out.show()
        source_img = Image.open("input.jpg").convert("RGBA")
if __name__ == '__main__':
    print("Тест")