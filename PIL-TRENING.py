import PIL
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

#получаем изображение
image = Image.open("./topics/0.png").convert("RGBA")

image2text = Image.new("RGBA", )

if __name__ == "__main__":
    print("PILTRENING")